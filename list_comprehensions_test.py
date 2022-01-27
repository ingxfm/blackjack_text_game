card_list = [11, 10, 25, -5, 11, "a",3, 11]
# the new_card_list will change the element to 1 in every occurrence of the number 11.
new_card_list = [1 if item == 11 else item for item in player_card_list] 


######################################################################################
def deal_card():
    '''    Return a random card from an argument of list datatype.    '''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)    
    return card

# this list comprenhension executes the function deal_card() for every element in a range of 2 elements.
user_hand = [deal_card() for card in range(2)] #create a list with user's 2 cards.
