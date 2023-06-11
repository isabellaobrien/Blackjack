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
    player_cards = []
    computer_cards = []
    deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K',
    'A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K','A', 2,
    3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K','A', 2, 3, 4,
    5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    
    random.shuffle(deck)
    card = deck[0]
    print(card)
    deck.remove(card)


deal_cards()

# def calculate_score():



# def compare():



# def deal_again():