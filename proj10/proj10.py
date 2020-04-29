# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 00:38:42 2020

@author: ab43p
"""


''' This program allows the user to play the Montana card game, displaying a
tableau that adapts to different moves that a user might play & also shuffles,
all the while checking each move to see whether the user has won or decides to
quit. '''

#DO NOT DELETE THESE LINES
import cards, random
random.seed(100) #random number generator will always generate 
                 #the same random number (needed to replicate tests)

def initialize():
    ''' This function creates an empty tableau using a list of 4 lists (rows).
    It then uses the cards class to create and shuffle a deck, and iterators
    to place cards randomly into each list or row. Returns the tableau'''
    
    tableau = [[],[],[],[]] # list of 4 empty lists
    deck = cards.Deck() # creates deck from Deck class in cards.py
    deck.shuffle() # shuffles it using Deck method 'shuffle'
    
    for lst in tableau: # for each of the 4 empty lists
        for num in range(13):
            lst.append(deck.deal()) # deal 13 cards

    return tableau
    
def display(tableau):
    '''
        This function displays the current state of the game.
        It display four rows of 13 cards with row and column labels.
        Ace is displayed with a blank.
        
        parameters: 
            tableau: data structure representing the tableau 
        
        Returns: None
    '''

    print("{:3s} ".format(' '), end = '')
    for col in range(1,14):
        print("{:3d} ".format(col), end = '')
    print()
        
    for r,row_list in enumerate(tableau):
        print("{:3d}:".format(r+1), end = '')
        for c in row_list:
            if c.rank() == 1:
                print("  {}{}".format(' ',' '), end = '')
            else:
                print("{:>4s}".format(str(c)),end = '')
        print()

def validate_move(tableau,source_row,source_col,dest_row,dest_col):
    ''' 
    This function validates each move the player tries to make, using the
    rules of Montana (Can't move to a non-empty space, can't move to the left-
    most column unless card is of rank 2, etc).
    
    Parameters: 
        tableau ; data structure of the tableau / cards
        source_row, source_col ; the source card's location
        dest_row, dest_col ; the desired destination location
    
    Returns: 
        Boolean regarding if the move is valid (True) or not (False)
    '''
    
    if tableau[dest_row][dest_col].rank() != 1: # if destination isn't an ace
        return False
    elif tableau[source_row][source_col].rank() == 2 and dest_col == 0:
        return True # if the card is of rank 2 it can go to left-most column
    # if the dest_col isn't the left-most, if the card being moved has the same
    # suit as the card to the left of the destination's, and if the source's
    # rank is 1 more than the card to the left of the destination : 
    elif dest_col != 0 and tableau[source_row][source_col].suit() \
        == tableau[dest_row][dest_col - 1].suit() and tableau[source_row]\
          [source_col].rank() == (tableau[dest_row][dest_col - 1].rank() + 1):
              return True # the move is valid
    else:
        return False

def move(tableau,source_row,source_col,dest_row,dest_col):
    ''' This function calls validate_move() to determine whether if a move is
    valid. If valid, the function swaps the 2 cards places on the tableau.
    
    Parameters:
            tableau ; data structure of the tableau / cards
            source_row & source_col ; the location of the card being moved
            dest_row & dest_col ; the location being moved to
    Returns:
            true boolean if the move was completed
            false boolean if the move was invalid & therefore wasn't done'''
            
    # calls validate_move(), gets True or False back
    valid = validate_move(tableau, source_row, source_col, dest_row, dest_col)
    if valid == True:
        empty_suit = tableau[dest_row][dest_col].suit() # suit of ace spot
        empty_rank = 1 # ace rank
        card_suit = tableau[source_row][source_col].suit() # source's suit
        card_rank = tableau[source_row][source_col].rank() # source's rank
        # initializes the source card to have the ace's characteristics
        tableau[source_row][source_col].__init__(empty_rank, empty_suit)
        # initializes the destination card to have the source's characteristics
        tableau[dest_row][dest_col].__init__(card_rank, card_suit)
        return True
    else:
        return False
    
def shuffle_tableau(tableau):
    ''' This function develops lists of cards and makes use of iterators to
    seek the cards in the tableau that need to be shuffled, to then shuffle
    them, to then redistribute them back into the tableau without impacting 
    cards that are in appropriate spaces, so as not to harm user progress.
    
    Parameters:
            tableau ; data structure of the tableau / cards
    Returns:
            none ; just rearranges the tableau'''
    shuffle = [] 
    aces = [] # aces will be put here
    for index, lst in enumerate(tableau):
        
        card_1 = lst[0]
        other_index = 0
        rank = 2 # initializes rank to 2 for each list
        if card_1.rank() == 2: # if 1st card is a 2
            # while card in lst at each index (increases inside while suite)
            # has same suit as first card & the rank increases with each card
            while lst[other_index].suit() == card_1.suit() and \
               rank == lst[other_index].rank():
                   
                   rank += 1 # makes loop check next higher rank
                   other_index += 1 # makes loop check next card in list
                   # for last card's rank (13) it will become 14, this fixes it
                   if rank == 14: # no such thing as card with rank 14
                       rank = 1 # sets rank to 1
            else:
                # if the cards aren't of same suit and in order, the tableau at
                # whatever index (or list) this occurs will then be equivalent
                # to all of the cards up to this point where conditions not met
                tableau[index] = lst[:other_index]
                # the list of cards we want to shuffle will then be the rest of
                # the cards in whichever list in the tableau is being checked
                shuffle.extend(lst[other_index:])
        else:
            # if it doesn't happen at all, the shuffle list will be the entire
            # list of cards for that index of the tableau's rows, and therefore
            # the tableau at that list will become empty, ready for new cards
            shuffle.extend(lst[:])
            tableau[index] = []
    
    # this line shuffles the list of cards we want shuffled, 'shuffle'
    random.shuffle(shuffle)
    for crd in shuffle:
        if crd.rank() == 1: # if the card is an ace
            aces.append(crd)
    # for some reason when shuffle.remove(crd) is in the if statement directly
    # above, it doesn't work, so a new for loop was needed to remove aces
    for crd in aces: 
        shuffle.remove(crd)
    
    index = 1
    for lst in tableau:
        # remaining # of cards that will be needed in a few lines
        remaining = 12 - len(lst)
        # if index <= len(aces): # guarantees no index error
        ace = aces[index - 1] # starts = 0, increases index for each list
        index += 1 # makes sure next iteration will use the next index val
        
        lst.append(ace) # appends whichever ace @ the index @ the iteration
        lst.extend(shuffle[:remaining]) # adds correct # of shuffled cards
        shuffle = shuffle[remaining:] # list only has cards it still has
    
def check_win(tableau):
    ''' This function checks to see if the tableau reflects the win conditions
    of the game.
    
    Parameters:
            tableau ; data structure of the tableau / cards
    Returns:
            false boolean if any win conditions aren't met (ex: 1st card != 2)
            true boolean if all win conditions are met (if false not found) '''
    
    for lst in tableau:
        suit = lst[0].suit() # judging suite of row by first card's suit
        for index,card in enumerate(lst[:-2]):
            
             # except for the ace at the end
            # if the first card in the row isn't a 2  
            if lst[0].rank() != 2:
                # print("Hi")
                return False
            # if the last card in the row isn't an ace
            elif len(lst) == 13 and lst[-1].rank() != 1: # rows 13 cards long
                # print("bye")
                return False
            # test case in mimir has space issue
            elif len(lst) == 12 and lst[-1].rank() != 13: # if only 12 cards:
                # check for last card being a king        # ^ mimir error ^
                # print("shmie")
                return False
            # if each card's rank isn't one more than the previous card's
            elif lst[index + 1].rank() != lst[index].rank()+1:
                # print("die")
                return False
            # if each card's suit (excl. ace) isn't the same as the first card
            elif lst[index + 1].suit() != suit:
                # print("kai")
                return False
    return True
             
def main():
    ''' This function calls the other functions in proper order along with 
    various messages & errors, allowing the user to play Montana. 
    
    Parameters / Returns ; none '''
    
    tableau = initialize() # initializes tableau
    print("Montana Solitaire.") # header
    display(tableau) # displays
    choice = input("Enter choice:\n (q)uit, (s)huffle, or space-separated:"\
                   " source_row,source_col,dest_row,dest_col: ") 
    shuffle_count = 0 # tracker of how many times user shuffles
    while not choice: # if empty input
        print("Error: invalid input.  Please try again.")
        choice = input("Enter choice:\n (q)uit, (s)huffle, or " \
                               "space-separated: source_row,source_col," \
                                   "dest_row,dest_col: ")
    while type(choice) == str:
        # checks to see if input is alphabetic
        if choice.isalpha():
            # exercises quit option
            if choice.lower() == 'q':
                again = input("Do you want to play again (y/n)?") 
                if again.lower() == 'y': # user wants to play again
                    tableau = initialize()
                    print("Montana Solitaire.")
                    display(tableau)
                    choice = input("Enter choice:\n (q)uit, (s)huffle, or "\
                                   "space-separated: source_row,source_col,"\
                                       "dest_row,dest_col: ")
                else: # user doesn't want to play again, ends loop
                    print("Thank you for playing.")
                    choice = 100
            # exercises shuffle option
            elif choice.lower() == 's':
                shuffle_count += 1 # adds to shuffle counter
                if shuffle_count <= 2: # can only shuffle twice in one game
                    shuffle_tableau(tableau) # shuffles
                    display(tableau) # displays
                    choice = input("Enter choice:\n (q)uit, (s)huffle, or "\
                                   "space-separated: source_row,source_col,"\
                                       "dest_row,dest_col: ")
                else: # can't shuffle 3+ times in a game
                    print("No more shuffles remain.")
                    choice = input("Enter choice:\n (q)uit, (s)huffle, or "\
                                   "space-separated: source_row,source_col,"\
                                       "dest_row,dest_col: ")
                
                
                
            # no other alphabetic options, prints an error & reprompts
            else:
                print("Error: invalid input.  Please try again.")
                choice = input("Enter choice:\n (q)uit, (s)huffle, or " \
                               "space-separated: source_row,source_col," \
                                   "dest_row,dest_col: ")
        # makes sure the entire input without spaces are just numbers
        elif (choice.replace(' ','')).isdigit():
            lst = []
            for item in choice.split():
                lst.append(item)
            if len(lst) == 4:
                source_row = int(lst[0]) - 1
                source_col = int(lst[1]) - 1
                dest_row = int(lst[2]) - 1 
                dest_col = int(lst[3]) - 1
                if 0 <= source_row <= 3 and 0 <= dest_row <= 3 and 0 <= \
                    source_col <= 12 and 0<= dest_col <= 12:
                    m = move(tableau,source_row,source_col,dest_row,dest_col)
                    if m == True: # if move was valid & therefore played
                        display(tableau)
                        check = check_win(tableau)
                        if check: # if check_win returns True
                            print("You won!")
                            again = input("Do you want to play again (y/n)?")
                            if again.lower() == 'y':
                                tableau = initialize() # reinitializes
                                print("Montana Solitaire.") # retitles
                                display(tableau) # redisplays
                                choice = input("Enter choice:\n (q)uit, "\
                                        "(s)huffle, or space-separated:"\
                                        " source_row,source_col,"\
                                            "dest_row,dest_col: ")
                            else: # thanks user, stops loop 
                                print("Thank you for playing.")
                                choice = 100
                        else: # reprompts normally if user move didn't win game
                            choice = input("Enter choice:\n (q)uit, (s)huffle"\
                                           ", or space-separated: source_row,"\
                                              "source_col,dest_row,dest_col: ")
                    else: # error if the user's move isn't valid
                        print("Error: invalid move.  Please try again.")
                        choice = input("Enter choice:\n (q)uit, (s)huffle, or"\
                                   " space-separated: source_row,source_col,"\
                                       "dest_row,dest_col: ")
                else: # error if user inputs a row/column that doesn't exist
                    print("Error: row and/or column out of range. "\
                          "Please Try again.")
                    choice = input("Enter choice:\n (q)uit, (s)huffle, or "\
                               "space-separated: source_row,source_col,"\
                                   "dest_row,dest_col: ")
            else: # error if 4 input numbers aren't received
                print("Error: invalid input.  Please try again.")
                choice = input("Enter choice:\n (q)uit, (s)huffle, or "\
                               "space-separated: source_row,source_col,"\
                                   "dest_row,dest_col: ")
        else: # error msg if choice isn't numeric format or alphabetical letter
                print("Error: invalid input.  Please try again.")
                choice = input("Enter choice:\n (q)uit, (s)huffle, or "\
                               "space-separated: source_row,source_col,"\
                                   "dest_row,dest_col: ")
            
if __name__ == "__main__":
    main()  