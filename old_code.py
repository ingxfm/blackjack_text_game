from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def do_you_want_to_play_blackjack():
    want_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") ##make this into a function
    return want_play

def deal_cards_start():
    '''
    This function deals cards at the beginning of the game when the user selects to play.
    '''
    user_hand = random.choices(cards, k=2) #print user's 2 cards.
    user_score = sum(user_hand)
    print(f"Your cards are: {user_hand}. Current score: {user_score}.\n")
    pc_hand = random.choices(cards, k=2) #print pc's first card only. The 2nd one should be hidden.
    print(f"The broker\'s first card is {pc_hand[0]}.\n")    
    dictionary_hands = {
        "user": {
            "hand": user_hand,
            "score": user_score
        },
        "broker": {
            "hand": user_hand,
            "score": user_score,
        }
    }
    # print(dictionary_hands["user"]["hand"])
    return dictionary_hands

def get_another_card(cards):
    '''
    This function takes another card from the deck.
    '''
    want_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    if want_another_card == "n":
        #compare
        #over_21 ?
        print("work")
    else:
        another_card = random.choice(cards)
        return another_card

def compare_user_broker(score_user, score_broker, final_hand_user, final_hand_broker):
    '''
    This function compares the score of the user's hand and the score of the broker's hand.
    '''
    if score_user == score_broker:
        print(f"Your final hand: {final_hand_user}, final score: {score_user}\n")
        print(f"The broker's final hand: {final_hand_broker}, final score: {score_broker}\n")
        print("It's a draw.")
        do_you_want_to_play_blackjack()# call function want_to_play
    elif score_user < score_broker:
        print(f"Your final hand: {final_hand_user}, final score: {score_user}\n")
        print(f"The broker's final hand: {final_hand_broker}, final score: {score_broker}\n")
        print("You lose.")
        # call function want_to_play
    elif score_user > score_broker:
        print(f"Your final hand: {final_hand_user}, final score: {score_user}\n")
        print(f"The broker's final hand: {final_hand_broker}, final score: {score_broker}\n")
        print("You win.")
        # call function want_to_play
    else:
        return "Invalid results. Houston, we have a problem."






want_play = do_you_want_to_play_blackjack()

if want_play == "n":
    print("Good bye.")
else:
    print(logo)
    starting_hands = deal_cards_start()
    # print(type(starting_hands))    
    next_card = get_another_card(cards) #do you want another card?????
    print(next_card)
    user_hand = 
    #print(dictionary_hands["user"]["hand"])#.append(next_card)



    #do_something_else




####################my old function
# def add_scores(player_card_list):
#     '''    Add upp the values in a hand: list datatype.    '''
#     score = sum(player_card_list)
#     if score == 21 and len(player_card_list) == 2:
#         return 0  #return stops the execution of the function
#     if 11 in player_card_list and score > 21:
#         # new_card_list = [1 if item == 11 else item for item in player_card_list] 
#         # this was nice, but maybe you do not want to convert every 11 into 1. Her method is better.
#         index = player_card_list.index(11)
#         player_card_list[index] = 1
#         print(player_card_list)
#         print(sum(player_card_list))


# want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") ##make this into a function
# if want_to_play == "y":
#     playing = 1
# else:
#     playing = 0
#     print("Select 'y' to play, next time. Good bye.")
