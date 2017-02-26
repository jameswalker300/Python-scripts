# Battleships game
	#edited Feb17


number_attempts = 10
board_size = 3


# Create Ocean (Game Board)
from random import randint

board = []  #empty list 

for x in range(board_size):
    board.append(["O"] * board_size)     #5 by 5 grid

def print_board(board):
    for row in board:
        print " ".join(row)     # get rid of quotation marks



# Introduce game
print "Let's play Battleships!"
print " "
print "There are 2 battleships of size 1 by 1 in an ocean with coordinates 0 - %d by 0 - %d.  " %(board_size-1,board_size-1)
print "You have %d attempts to sink them." % number_attempts
print "Good luck!"
print " "
print "Ocean"
print_board(board)
print " "


# Randomly generate location for both ships
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)
    
# Generate ships location
ship1_row = random_row(board)
ship1_col = random_col(board)

ship2_row = random_row(board)
ship2_col = random_col(board)

"""
# Print ships location (for debugging only, remove for actual game!)
print "Ship 1 location"
print ship1_row
print ship1_col
print "Ship 2 location"
print ship2_row
print ship2_col
print " "
"""

# Tally number of ships sunk
number_sunk = 0


# Create turns
for turn in range(number_attempts):
    print "--------------------------------------------------"
    print "Turn", turn + 1

    guess_row = raw_input("Guess Row:")
    guess_col = raw_input("Guess Col:")

    guess_row = int(guess_row)
    guess_col = int (guess_col)

    # Correct guesses 
		#Ship 1
	if guess_row == ship1_row and guess_col == ship1_col:
        print " "
        print "Congratulations! You sunk ship 1"
        print " "
        number_sunk = number_sunk + 1
        board[guess_row][guess_col] = "1"
        print_board(board)
        print " "
		
        #Ship 2
    elif guess_row == ship2_row and guess_col == ship2_col:
        print " "
        print "Congratulations! You sunk ship 2"
        print " "
        number_sunk = number_sunk + 1
        board[guess_row][guess_col] = "2"
        print_board(board)
        print " "
        
    # Incorrect, or disallowed guesses
    else:
        
        # Out of range
        if guess_row < 0 or guess_row > (board_size - 1) or guess_col < 0 or guess_col > (board_size - 1):
            print "Oops, that's not even in the ocean."
            
        # Not an integer
        elif type(guess_row) is not int:
            print "Error, row input must be integer value"
        elif type(guess_col) is not int:
            print "Error, column input must be integer value"    
            
            
        # Repeated guess
        elif board[guess_row][guess_col] == "1" or board[guess_row][guess_col] == "2":
            print "You guessed that one already."
            
        # Missed both ships
        else:
            print "You missed the battleships!"
            board[guess_row][guess_col] = "X"
        if turn == (number_attempts -1):
            print "Game Over, you sunk no ships :("
        
        print_board(board)
        print " "
    
    # End game if both ships are sunk             
    if number_sunk == 2:
        print "Great job, you sunk both ships"
        #break
