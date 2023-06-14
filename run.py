import gspread
from google.oauth2.service_account import Credentials
import random
from art import blackjack
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Blackjack1')

deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
    'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K','A', 2,
    3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K','A', 2, 3, 4,
    5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

def deal_cards(deck):
    """returns the first card from a shuffled deck of cards.
     The delt card is then removed from the deck."""
    
    random.shuffle(deck)
    card = deck[0]
    deck.remove(card)
    return card
    

def calculate_score(cards):
    """Takes a list of cards and checks if there's a J,Q or K, if 
    there is it adds 10 to the score (score starts at 0). If there's 
    an ace and the score is above 11 already, 
    1 is added if not 11 is added. And finally it returns the score 
    calculated from the cards"""
    score = 0
    for card in cards:
        if card == 'J' or card == 'Q' or card == 'K':
            score += 10
        elif card == 'A':
            if score <= 11:
                score += 11
            else:
                score += 1
        else:
            score += card
     
    # if score == 21 and len(cards) == 2:
    #     return 0

    return score

print(blackjack)
print("Welcome to Blackjack!")
username = input("What's your user name?\n")

def update_sheet(data, worksheet):
    """updates the worksheets"""
    worksheet.append_row(data)

def compare(player_score, computer_score):
    """Compares the user and users score to see who wins"""
    if player_score == computer_score:
        return "It's a Draw\n"
    elif player_score == 21:
        return f"Blackjack {username} won!\n"
    elif computer_score == 21:
        return f"The computer scored a blackjack, {username} lose.\n"
    elif player_score > 21:
        return f"{username} went over, {username} lost\n"
    elif computer_score > 21:
        return f"{username} won, the computer went over!\n"
    elif player_score > computer_score:
        return f"{username} won!\n"
    else:
        return f"{username} lost.\n"



players = SHEET.worksheet("players")
update_sheet([username], players)

def play(): 
    """runs the game. It deals two cards to the user and 
    two to the computer, it only reveals one of the computers cards. 
    If no one has scored a blackjack or goen over 21 teh game continues, the user can draw another card.
    The computer draws another cards if the score is below 16 and not a blackajack"""
    # make sure it's really copying original deck, not by referance. print should be 52
    play_deck = deck
    player_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        player_cards.append(deal_cards(play_deck))
        computer_cards.append(deal_cards(play_deck))

    while not game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"These are your current cards: {player_cards}, this is your current score: {player_score}")
        print(f"This is the computer's first card: {computer_cards[0]}")

        if computer_score == 21 or player_score == 21 or player_score > 21:
            game_over = True
        else:
            should_continue = input("Do you want to draw another card? type 'y' or 'n': \n")
            if should_continue == 'y':
                player_cards.append(deal_cards(play_deck))
            elif should_continue == 'n':
                game_over = True
            else:
                print("Error, invalid data.Please input valid data. type 'y' or 'n'!!!\n")

    while computer_score < 16:
        computer_cards.append(deal_cards(play_deck))
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand: {player_cards}, your final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, computer's final score: {computer_score}")
    outcome = compare(player_score, computer_score)
    print(outcome)

    # this section updates the worksheets and returns the leaderboard 
    # player_final_scores = SHEET.worksheet('player_final_scores')
    # update_sheet([player_score], player_final_scores)
    # computer_final_scores = SHEET.worksheet('computer_final_scores')
    # update_sheet([computer_score], computer_final_scores)
    # winners = SHEET.worksheet('winners')
    # update_sheet([outcome], winners)
    # for i in reversed(range(1, 3)):
    #     player = players.row_values(i)
    #     player_final_score = player_final_scores.row_values(i)
    #     computer_final_score = computer_final_scores.row_values(i)
    #     winner = winners.row_values(i)

    #     print(f"{player[0]} scored: {player_final_score[0]}, computer scored: {computer_final_score[0]} -- {winner[0]}")

#if the user decides to play another game the name is not saved a second time
#  but the score is. I've tried updating the worksheet again when the user decides
#to play again but it saves the username even if the user doesn't want to play again

#I can't show the most recent scores with range. Ineed to know exactly how many people have played 
# and how many times.
while input("Do you want to play a game of blackjack? type 'y' or 'n': \n") == 'y':
    play()
    





