from os import system, name
from art import logo
import random

def clear():
    '''    Clears the screen.    '''
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")    

def deal_card():
    '''    Return a random card from an argument of list datatype.    '''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)    
    return card

def add_scores(player_card_list):
    '''    Add upp the values in a hand: list datatype.    '''
    score = sum(player_card_list)
    if score == 21 and len(player_card_list) == 2:
        return 0  #return stops the execution of the function
    if 11 in player_card_list and score > 21:
        index = player_card_list.index(11)
        player_card_list[index] = 1
    return score

def compare(user_scoring, broker_scoring):
    '''    Compare user scores agains the broker scores and prints results.    '''
    if user_scoring == broker_scoring:
        print(f"\n    Your final score: {user_scoring}. Broker's final score: {broker_scoring}.\n")
        print("    Both have the same score. It's a draw.\n")
    elif broker_scoring == 0: #0 represents blackjack in this game as the func returns that by design when score is 21.
        print(f"\n    Your final score: {user_scoring}. Broker's final score: {broker_scoring}.\n")
        print("    The broker has a Black Jack. You lose. She wins.\n")
    elif user_scoring == 0: # 0 represents black jack.
        print(f"\n    Your final score: {user_scoring}. Broker's final score: {broker_scoring}.\n")
        print("    You have a Black Jack. You win.\n")
    elif user_scoring > 21:
        print(f"\n    Your final score: {user_scoring}. Broker's final score: {broker_scoring}.\n")
        print("    Your score is over 21. You lose.\n")
    elif broker_scoring > 21:
        print(f"\n    Your final score: {user_scoring}. Broker's final score: {broker_scoring}.\n")
        print("    The broker's score is over 21. You win.\n")
    elif broker_scoring > user_scoring:
        print(f"\n    Your score is {user_scoring} and the broker's score is {broker_scoring}. You lose.\n")
    elif broker_scoring < user_scoring:
        print(f"\n    Your score is {user_scoring} and the broker's score is {broker_scoring}. You lose.\n")

def blackjack_game():
    '''   Play the text-based blackjack game.   '''
    playing = True

    user_hand = [deal_card() for card in range(2)] #create a list with user's 2 cards. #line_revised, it works as intended.
    broker_hand = [deal_card() for card in range(2)] #create a list with broker's 2 cards. #line_revised, it works as intended.

    while playing:
        user_score = add_scores(player_card_list=user_hand)
        broker_score = add_scores(player_card_list=broker_hand)
        print(f"\nUser's hand: {user_hand}, current score: {user_score}.\n")
        if broker_score == 0:
            print(f"Broker's first card: {broker_hand[0]}.\n")
        else:
            print(f"Broker's first card: {broker_hand[0]}.\n")

        if user_score == 0 or broker_score == 0 or user_score > 21:
            playing = False
        else:
            another_card = input("Do you want another card? Enter 'y' or 'n' for yes or no: ")
            if another_card == "y":
                user_hand.append(deal_card())
            else:
                playing = False

    while broker_score != 0 and broker_score < 17:
        broker_hand.append(deal_card())
        broker_score = add_scores(player_card_list=broker_hand)
    # print(f"\nBroker's hand: {broker_hand}, current score: {broker_score}.\n") #test broker's hand
    compare(user_scoring=user_score, broker_scoring=broker_score)

play_game = True
while play_game:
    play_game = input("Do you want to play Blackjack? Type 'y' for yes or 'n' for no: ")
    if play_game == "n":
        play_game = False
        print("Good bye!")        
    else:
        clear()
        print(logo)
        blackjack_game()   
        
