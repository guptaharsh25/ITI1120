import random

##################################
#   GENERAL UTILITY FUNCTIONS    #
##################################

# done
def shuffle_deck(deck):
    """(list of str)->None
       Shuffles the given list of strings representing the playing deck
    """
    # YOUR CODE GOES HERE
    print("Shuffling the deck... ")
    # used help(random) in IDLE to find this method.
    random.shuffle(deck)

# done
def create_board(size):
    """int->list of str
       Precondition: size is even positive integer between 2 and 52
       Returns a rigorous deck (i.e. board) of a given size.
    """
    board = [None]*size 

    letter='A'
    for i in range(len(board)//2):
          board[i]=letter
          board[i+len(board)//2 ]=board[i]
          letter=chr(ord(letter)+1)
    return board

# done
def print_board(a):
    """(list of str)->None
       Prints the current board in a nicely formatted way
    """
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')

# done
def wait_for_player():
    '''()->None
    Pauses the program/game until the player presses enter
    '''
    input("\nPress enter to continue. ")
    print("\n\n\n\n\n\n\n\n\n\n")

# done
def print_revealed(discovered, p1, p2, original_board):
    '''(list of str, int, int, list of str)->None
    Prints the current board with the two new positions (p1 & p2) revealed from the original board
    Preconditions: p1 & p2 must be integers ranging from 1 to the length of the board
    '''
    # YOUR CODE GOES HERE

    new_board = discovered
    new_board[p1] = original_board[p1]
    new_board[p2] = original_board[p2]

    print_board(new_board)


#############################################################################
#   FUNCTIONS FOR OPTION 2 (with the board being read from a given file)    #
#############################################################################

# done
def read_raw_board(file):
    """str->list of str
    Returns a list of strings representing a deck of cards that was stored in a file.
    The deck may not necessarily be playable
    """
    raw_board = open(file).read().splitlines()
    for i in range(len(raw_board)):
        raw_board[i]=raw_board[i].strip()
    return raw_board

# done
def clean_up_board(l: list) -> list:
    """list of str->list of str

    The functions takes as input a list of strings representing a deck of cards.
    It returns a new list containing the same cards as l except that
    one of each cards that appears odd number of times in l is removed
    and all the cards with a * on their face sides are removed
    """
    print("\nRemoving one of each cards that appears odd number of times and removing all stars ...\n")
    playable_board=[]

    # YOUR CODE GOES HERE
    for i in range(len(l)):
        if l[i] != "*":
            if (l[i:].count(l[i]) + playable_board.count(l[i])) % 2 == 0:
                playable_board.append(l[i])
    
    return playable_board

# done
def is_rigorous(l: list):
    """list of str->True or None
    Returns True if every element in the list appears exactly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: Every element in the list appears even number of times
    """

    # YOUR CODE GOES HERE
    if len(l) == 0:
        return True
    else:
        for i in range(len(l)):
            if l.count(l[i]) > 2:
                return False

        return True

####################################################################
# done
def play_game(board):
    """(list of str)->None
    Plays a concentration game using the given board
    Precondition: board a list representing a playable deck
    """

    print("Ready to play ...\n")

    # this is the function that plays the game
    # YOUR CODE GOES HERE

    guesses = 0

    current_board = ['*'] * len(board)
    trial_board = current_board

    first_time = True
    while trial_board != board:
        if first_time:
            print_board(trial_board)
        print()
        print("Enter two distinct positions on the board that you want revealed.")
        print("i.e. two integers in the range [1, " + str(len(board)) + "]")

        p1 = int(input("Enter position 1: "))
        p2 = int(input("Enter position 2: "))

        if trial_board[p1-1] == board[p1-1] or trial_board[p2-1] == board[p2-1]:
            print("One or both of your chosen positions has already been paired.")
            print("Please try again. This guess did not count. Your current number of guesses is " + str(guesses) + ".")
            print()
            first_time = False

        elif p1 == p2:
            print("You chose the same positions.")
            print("Please try again. This guess did not count. Your current number of guesses is " + str(guesses) + ".")
            print()
            first_time = False

        else:
            trial_board[p1 - 1] = board[p1 - 1]
            trial_board[p2 - 1] = board[p2 - 1]
            print_board(trial_board)
            wait_for_player()
            guesses += 1
            if trial_board[p1 - 1] != trial_board[p2 - 1]:
                trial_board[p1 - 1] = '*'
                trial_board[p2 - 1] = '*'
            first_time = True

    if trial_board == board:
        print("Congratulations! You completed the game with " + str(guesses) + " guesses. That is " + str(int(guesses - (len(board) / 2))) + " more than the best possible.")

# Copied from Assignment #1
def ascii_name_plaque(name: str):
    """
        Prints a name plaque.
    """
    nameLength = len(name)

    print("*****" + ("*" * nameLength) + "*****")
    print("*    " + (" " * nameLength) + "    *")
    print("*  __" + name + "__  *")
    print("*    " + (" " * nameLength) + "    *")
    print("*****" + ("*" * nameLength) + "*****")


# main
if __name__ == "__main__":
    ascii_name_plaque("Welcome to my Concentration game")
    print()
    print()
    # YOUR CODE TO GET A CHOICE 1 or CHOICE 2 from a player GOES HERE
    print("Would you like (enter 1 or 2 to indicate your choice):")
    selection = int(input("(1) me to generate a rigorous deck of cards for you\n(2) or, would you like me to read a deck from a file?\n"))
    while selection != 1 and selection != 2:
        selection = int(input(str(selection) + " is not an existing option. Please try again. Enter 1 or 2 to indicate your choice:\n"))

    # YOUR CODE FOR OPTION 1 GOES HERE
    if selection == 1:
        print("You chose to have a rigorous deck generated for you.")
        print()
        print("How many cards do you want to play with?")
        size = int(input("Enter a number between 2 and 52: "))
        print()
        while num_cards % 2 != 0 or num_cards > 52 or num_cards < 2:
            print("How many cards do you want to play with?")
            num_cards = int(input("Enter a number between 2 and 52: "))
            print()
        print()
        print()
        wait_for_player()
        board = create_board(size)
        shuffle_deck(board)
        play_game(board)

    # YOUR CODE FOR OPTION 2 GOES HERE
    elif selection == 2:
        print("You chose to load a deck of cards from a file")
        file = input("Enter the name of the file: ")
        file = file.strip()
        print()
        board = read_raw_board(file)
        print()
        board = clean_up_board(board)
        if is_rigorous(clean_up_board(board)):
            statement = "This deck is now playable and rigorous and it has " + str(len(board)) + " cards."
        else:
            statement = "This deck is now playable but not rigorous and it has " + str(len(board)) + " cards."
        ascii_name_plaque(statement)
        print()

        wait_for_player()
        shuffle_deck(board)
        wait_for_player()
        if len(board) == 0:
            print("The resulting board is empty.")
            print("Playing Concentration game with an empty board is impossible.")
            print("Good bye")
        else:
            play_game(board)



