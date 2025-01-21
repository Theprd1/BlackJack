logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)
import random
your_cards=[]
computer_cards=[]
deck=[1,11,2,3,4,5,6,7,8,9,10,10,10,10]
response= input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
# if response=='y':
def my_pick():
    '''Takes input from the Users and does everything needed and returns the winner and their score'''
    your_cards.extend(random.sample(deck, 2))
    print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
    computer_cards = random.sample(deck, 1)
    print(f"Computer's first card: {sum(computer_cards)}")

    pick= True
    while pick:
        if sum(your_cards)>21:
            print("You Lose!")
            break
        another_card = input("Type 'y' to get another card, type 'n' to pass:")
        if another_card == 'y':
            your_cards.extend(random.sample(deck, 1))
            print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
            print(f"Computer's first card: {sum(computer_cards)}")
        elif another_card == 'n':
            pick= False
            computer_pick()
def computer_pick():
    pick= True
    while pick:
        if sum(computer_cards)>21:
            pick= False
            of()
            print("Opponent went Over! You Win!")
        elif sum(computer_cards)<17:
            computer_cards.extend(random.sample(deck, 1))
        elif sum(your_cards)==sum(computer_cards):
            pick = False
            of()
            print("Draw")
        elif sum(your_cards)<sum(computer_cards):
            of()
            pick = False
            print("Dealer Wins!")
        elif sum(your_cards)>sum(computer_cards):
            of()
            pick = False
            print("You Win!")
    return
def of():
    print(f"Your Final cards: {your_cards}, Final score: {sum(your_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")

my_pick()
