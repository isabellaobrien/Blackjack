import gspread
from google.oauth2.service_account import Credentials
import random
# SCOPE = [
#     "https://www.googleapis.com/auth/spreadsheets",
#     "https://www.googleapis.com/auth/drive.file",
#     "https://www.googleapis.com/auth/drive"
#     ]

# CREDS = Credentials.from_service_account_file('creds.json')
# SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# SHEET = GSPREAD_CLIENT.open('Blackjack1')

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
    return score 
    if score == 21 and len(cards) == 2:
        return 0
calculate_score(['A', 10])



# def compare():

player_cards = []
computer_cards = []

for i in range(2):
    player_cards.append(deal_cards())
    computer_cards.append(deal_cards())

player_score = calculate_score(player_cards)
computer_score = calculate_score(computer_cards)
print(f"Your current cards are: {player_cards}, your current score is: {player_score}")
print(f"The computer's first card is: {computer_cards[0]}")
