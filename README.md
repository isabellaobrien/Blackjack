# Blackjack
Blackjack is a game that runs in the terminal. It can be played in a mock terminal on heroku.
Users play against the computer with a deck of 52 cards. The user needs to try and score a blackjack which is 21 points.

[Link to live project](https://jackblack-21-56ff233614fb.herokuapp.com/)

![screenshots of the game on on different screen sizes](images/responsive.png)
## How to pay
This terminal game is based on the famous blackjack casino game. [find out more about blackjack](https://en.wikipedia.org/wiki/Blackjack).

In this version the user inputs their username and two cards from a shuffled deck are drawn for the player and the computer.

The player can see both of their cards but only the computer’s first card.

The cards from 2 to 10 have face value, whereas the cards J, Q and K have a value of 10 and A has a value of 11 or 1 based on the hand.

If the game is not over in the first hand, the player will be asked if they want to draw another card. 

The computer only draws another card if the score is less than 16. 

### How to win 
- If the player and the computer score the same, it's a Draw.
- If the player scores a blackjack, 21 points.
- If the computers scores a blackjack, the player loses.
- If the player scores above 21, they lose.
- If the computer scores above 21, the player wins.
- If the scores are both below 21 the highest one is te winner.

## Features
- Random card generantion: 
  - we start of with an organised deck of cards that gets shuffled.
  - we then deal the cards from the top of the deck as we would in person.
  - the cards dealt will be random.
- Play against the computer.
- Accepts user input and validates it.
  - the question will be asked until the input is satisfactory.
- Leaderboard:
  - it's in cronological order, the person that played last will be at the top.
  - it includes the player's username, the player's final score, the computer's final score and finally the outcome of the game. 

## Data model
I decided to create functions that to do smaller tasks within the game and call them inside of a larger function that runs the entire game.
 I created a function to:
 - deal the cards
 - calculate the score
 - compare the scores 
 - update the leaderboard
All of these functions are stored in the play function that allows the game to run.

## Testing
I have manually tested this project by:
- I've passed the code through a python linter and confirmed that there are no errors that inpact its functionality.
I used [Python syntax checker](https://extendsclass.com/python-tester.html).
- I've inputed incorrect data to check the data validation and it all works correctly.
- I've also tested the code in both the local termianl and heroku terminal.

### Remaining bugs
Initially every time the deal_cards() function was called it would deal a single card from a deck of 52, only one card was being removed from the deck. The function had no arguments and the deck was declared inside te function.
The function now has a deck of 52 cards as an argument, cards are removed from the deck once they've been dealt. I haven't been able to make a hard copy of the full deck to use every time the player wants to play again. If the player continues to select play agin at some point the deck will run out. A temporary solution is to run the game again, the scores won't be lost because they are all saved in the leaderboard.
This is definetly a bug I would like to fix for a future version of this game.

## Deployment
This project was deployed using CI's mock terminal in heroku.
- steps:
  - I made sure the libaries usedd where stored in the requirements.txt file.
  - I clicked on "create an app" in heroku, I named the app and selected my region.
  - I went to settings and added my creds.json file in order to protect my private information.
  - I added pythona and node.js as buildpacks.
  - I then went to settings, connected to git hub.
  - I then manually deployed my project.

## Credits
- the colored python library allowed me colour the text in the termial.
- [gspread documentation](https://docs.gspread.org/en/v5.1.0/api.html).
- [ascii text generator](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)