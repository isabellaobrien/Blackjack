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

def deal_cards():
    deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
    'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K','A', 2,
    3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K','A', 2, 3, 4,
    5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    
    random.shuffle(deck)
    card = deck[0]
    return card
    deck.remove(card)

def calculate_score(cards):
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
     
    if score == 21 and len(cards) == 2:
        return 0

    return score

def compare(player_score, computer_score):
    if player_score == computer_score:
        return "It's a Draw"
    elif player_score == 0:
        return "Blackjack you win!"
    elif computer_score == 0:
        return "The computer scored a blackjack, you lose."
    elif player_score > 21:
        return "You went over, you lose"
    elif computer_score > 21:
        return "You win, the computer went over!"
    elif player_score > computer_score:
        return "You win!"
    else:
        return "You lose."



def play(): 
    
    player_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        player_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"These are your current cards: {player_cards}, this is your current score: {player_score}")
        print(f"This is the computer's first card: {computer_cards[0]}")

        if computer_score == 0 or player_score == 0 or player_score > 21:
            game_over = True
        else:
            should_continue = input("Do you want to draw another card? type 'y' or 'n':\n ")
            if should_continue == 'y':
                player_cards.append(deal_cards())
                print(player_cards)
            elif should_continue == 'n':
                game_over = True
            else:
                print("Error, invalid data.Please input valid data. type 'y' or 'n'!!!\n")

    while computer_score != 0 and computer_score < 16:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand: {player_cards}, your final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, computer's final score: {computer_score}")
    print(compare(player_score, computer_score))


print(blackjack)
print("Welcome to Blackjack!")
username = input("What's your user name?\n")
while input("Do you want to play a game of blackjack? type 'y' or 'n': \n") == 'y':
    play()




# sheet1 = SHEET.worksheet('Sheet1')

# players = sheet1.col_values(1)
# player_final_score = sheet1.col_values(2) 
# computer_final_score = sheet1.col_values(3)
# outcome = sheet1.col_values(4)
# for i in range(1,5):
#     print(f"{players[i]} scored: {player_final_score[i]}, computer scored: {computer_final_score[i]} -- {outcome[i]}")


def update_sheet(data, worksheet):
    worksheet.append_row(data)

players = SHEET.worksheet("players")
update_sheet([username], players)