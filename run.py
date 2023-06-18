import gspread
from google.oauth2.service_account import Credentials
import random
from art import blackjack
from colored import fg


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


    return score

print(blackjack)
blue = fg('deep_sky_blue_1')
green = fg('pale_green_1b')
pink = fg('indian_red_1d')
yellow = fg('light_goldenrod_2b')

print(blue + "Welcome to Blackjack!")
username = input(green + "What's your user name?\n")

leaderboard = SHEET.worksheet('leaderboard')

def update_leaderboard(data):
    """updates the worksheets"""
    leaderboard.append_row(data)

def compare(player_score, computer_score):
    """Compares the user and users score to see who wins"""
    if player_score == computer_score:
        return  "Draw"
    elif player_score == 21:
        return f"Blackjack {username} won!"
    elif computer_score == 21:
        return f"The computer scored a blackjack"
    elif player_score > 21:
        return f"{username} went over, {username} lost"
    elif computer_score > 21:
        return f"{username} won, the computer went over!"
    elif player_score > computer_score:
        return f"{username} won!"
    else:
        return f"{username} lost."


def play(): 

    """runs the game. It deals two cards to the user and 
    two to the computer, it only reveals one of the computers cards. 
    If no one has scored a blackjack or goen over 21 teh game continues,
    the user can draw another card.The computer draws another cards if
    the score is below 16 and not a blackajack"""
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
        print(green + f"Your cards: {player_cards}, score: {player_score}")
        print(pink + f"Computer's first card: {computer_cards[0]}")

        if computer_score == 21 or player_score == 21 or player_score > 21:
            game_over = True
        else:
            should_continue = input(blue + "Do you want to draw another card? type 'y' or 'n': \n")
            if should_continue == 'y':
                player_cards.append(deal_cards(play_deck))
            elif should_continue == 'n':
                game_over = True
            else:
                print("Error, invalid data.Please input valid data. type 'y' or 'n'!!!\n")

    while computer_score < 16:
        computer_cards.append(deal_cards(play_deck))
        computer_score = calculate_score(computer_cards)
    print(green + f"Your final hand: {player_cards}, final score: {player_score}")
    print(pink + f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    outcome = compare(player_score, computer_score)
    print(yellow + outcome)
    print("\n")

    # updates leaderboard on google sheets
    update_leaderboard([username, player_score, computer_score, outcome])
    records = leaderboard.get_all_records()
    records.reverse()
    
    for i in range(len(records)):
        print(records[i])
        

want_to_play = 'y'
yes = ('y')
valid = ('y', 'n')
while want_to_play in yes:
    play()
    want_to_play = input(blue + "Do you want to play a game of blackjack? type 'y' or 'n': \n")
    while want_to_play not in valid:
        want_to_play = input("Error, invalid data.Please input valid data. type 'y' or 'n'!!!\n")

   
    






    





