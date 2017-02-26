__author__ = 'jameswalker300'

from random import randint
import os

# Feb17 edits
	#

def whole_game():
    #Introduce the game
    print " --------------- Welcome to Mastermind  --------------- "

    def print_instructions():
        print "You must guess the correct combination of 4 numbers ranging from 1 to 6"
        print "You only have 8 attempts"
        print "X - means correct number, correct position"
        print "O - means correct number, incorrect posistion"
        begin = 1
        print " "
    begin = raw_input("Press any key to begin")
    print "\n" * 50


    #### Make board ###########

    # board[1][1] to board[10][4] is turns

    #Create board###
    board = []  #empty list
    for x in range(10):
        board.append(["#"] * 7)     #
    for i in range(1,9):
        for j in range(1,5):
            board[i][j] = "O"

    #### create output text file ###
    score_output = open("mastermind_result_output.txt", "w")

    ###### Make feedback ########

    """
    #Feedbacks to append to
    feedback1 = " "
    feedback2 = " "
    feedback3 = " "
    feedback4 = " "
    feedback3 = " "
    feedback5 = " "
    feedback6 = " "
    feedback7 = " "
    feedback8 = " "

    feedback1 + "X"
    print feedback1"""


    """
    # Update feedback matrix every Turn
    def update_feedback_matrix():
        Feedback_matrix[1][0] = feedback1
        Feedback_matrix[2][0] = feedback2
        Feedback_matrix[3][0] = feedback3
        Feedback_matrix[4][0] = feedback4
        Feedback_matrix[5][0] = feedback5
        Feedback_matrix[6][0] = feedback6
        Feedback_matrix[7][0] = feedback7
        Feedback_matrix[8][0] = feedback8

    update_feedback_matrix()"""

    def sort_feedback():
        for i in range(1,9):
            Feedback_matrix[i][0] = ''.join(sorted(Feedback_matrix[i][0]))

    #Feedback matrix for turn looping
    Feedback_matrix = [[" " for x in range(1)] for x in range(10)]


    def print_board(board):
        row_count = 0
        for row in board:
            if row_count == 0:
                print " ".join(row), "Feedback"
            if row_count == 1:
                print " ".join(row),Feedback_matrix[row_count][0]
            if row_count == 2:
                print " ".join(row),Feedback_matrix[row_count][0]
            if row_count == 3:
                print " ".join(row),Feedback_matrix[row_count][0]
            if row_count == 4:
                print " ".join(row),Feedback_matrix[row_count][0]

            if row_count == 5:
                print " ".join(row),Feedback_matrix[row_count][0]
            if row_count == 6:
                print " ".join(row),Feedback_matrix[row_count][0]
            if row_count == 7:
                print " ".join(row),Feedback_matrix[row_count][0]
            if row_count == 8:
                print " ".join(row),Feedback_matrix[row_count][0]

            if row_count == 9:
                print " ".join(row),Feedback_matrix[row_count][0]
            if row_count == 10:

                print " ".join(row)
            row_count += 1


    ###################################



    #Generate numbers
    code_to_guess = str(randint(1,6)) + str(randint(1,6)) + str(randint(1,6)) + str(randint(1,6))



    #### Iterate turns
    for turn in range(1,9):

        print "Code to guess:%s" %code_to_guess + "\n" # for debugging only

        print_instructions()
        print "---------------------------------------------------"
        print "Turn", turn, "\n"
        sort_feedback()
        print_board(board)
        print "\n" * 5
        print " "

        # Ask for raw input
        current_guess = str(raw_input("Guess 4 numbers between 1 and 6:"))
        print "\n" * 5


        # Disallowed characters
        if current_guess == "":
            print " -------- Input error ---------"
            print "Oops, input 4 numbers in row eg 1111"
            print "Try again"


        elif len(current_guess) != 4:
            print " -------- Input error ---------"
            print "Oops, input 4 numbers in row eg 1111"
            print "Try again"

        # Code for if its not an int, doesn't work

            """for i in range(4):
                int_current = int(current_guess[i])
                if type(int(int_current)) != int:
                    print " -------- Input error ---------"
                    print "Oops, number %d wasn't an integer between 1 and 6." % (i + 1)
                    print " "

                elif int(current_guess[i]) < 1 or int(current_guess[i]) > 6:
                    print " -------- Input error ---------"
                    print "Oops, number %d wasn't an integer between 1 and 6." % (i + 1)
                    print " "
            """


        #If input is correct format
        else:
            #Print current guess to board
            for i in range(4):
                board[turn][i+1] = current_guess[i]

            print "\n" * 50




            ### Loop over iterations to assign feedback #####

            for i in range(4):
                # Correct colour, correct place
                if code_to_guess[i] == current_guess[i]:
                    Feedback_matrix[turn][0] = Feedback_matrix[turn][0] + "X"
                elif code_to_guess[i] == current_guess[0]:
                    Feedback_matrix[turn][0] = Feedback_matrix[turn][0] + "O"
                elif code_to_guess[i] == current_guess[1]:
                    Feedback_matrix[turn][0] = Feedback_matrix[turn][0] + "O"
                elif code_to_guess[i] == current_guess[2]:
                    Feedback_matrix[turn][0] = Feedback_matrix[turn][0] + "O"
                elif code_to_guess[i] == current_guess[3]:
                    Feedback_matrix[turn][0] = Feedback_matrix[turn][0] + "O"
                else:
                    Feedback_matrix[turn][0] = Feedback_matrix[turn][0] + ""



            """    if code_to_guess[i] == current_guess[i]:
                    Feedback_matrix[turn][0] = Feedback_matrix[turn][0] + "X"
                    places_found.append(i)
                elif code_to_guess[i] == current_guess[0]:
                    Feedback_matrix[turn][0] = Feedback_matrix[turn][0] + "O"
                elif code_to_guess[i] == current_guess[1]:
                    Feedback_matrix[turn][0] = Feedback_matrix[turn][0] + "O"
                elif code_to_guess[i] == current_guess[2]:
                    Feedback_matrix[turn][0] = Feedback_matrix[turn][0] + "O"
                elif code_to_guess[i] == current_guess[3]:
                    Feedback_matrix[turn][0] = Feedback_matrix[turn][0] + "O"
                else:
                    Feedback_matrix[turn][0] = Feedback_matrix[turn][0] + ""
                if code_to_guess[i] == current_guess[1]:
                    Feedback_matrix[turn][0] = Feedback_matrix[turn][0] + "X"
                elif code_to_guess[i] == current_guess[1]:
                    Feedback_matrix[turn][0] = Feedback_matrix[turn][0] + "O"
                elif code_to_guess[i] == current_guess[2]:

                    Feedback_matrix[turn][0] = Feedback_matrix[turn][0] + "O"
                elif code_to_guess[i] == current_guess[3]:
                    Feedback_matrix[turn][0] = Feedback_matrix[turn][0] + "O"
                else:
                    Feedback_matrix[turn][0] = Feedback_matrix[turn][0] + ""
                if code_to_guess[i] == current_guess[2]:
                    Feedback_matrix[turn][0] = Feedback_matrix[turn][0] + "X"
                elif code_to_guess[i] == current_guess[1]:
                    Feedback_matrix[turn][0] = Feedback_matrix[turn][0] + "O"
                elif code_to_guess[i] == current_guess[2]:
                    Feedback_matrix[turn][0] = Feedback_matrix[turn][0] + "O"
                elif code_to_guess[i] == current_guess[3]:
                    Feedback_matrix[turn][0] = Feedback_matrix[turn][0] + "O"
                else:
                    Feedback_matrix[turn][0] = Feedback_matrix[turn][0] + ""
                if code_to_guess[i] == current_guess[3]:
                    Feedback_matrix[turn][0] = Feedback_matrix[turn][0] + "X"
                elif code_to_guess[i] == current_guess[1]:
                    Feedback_matrix[turn][0] = Feedback_matrix[turn][0] + "O"
                elif code_to_guess[i] == current_guess[2]:
                    Feedback_matrix[turn][0] = Feedback_matrix[turn][0] + "O"
                elif code_to_guess[i] == current_guess[3]:
                    Feedback_matrix[turn][0] = Feedback_matrix[turn][0] + "O"
                else:
                    Feedback_matrix[turn][0] = Feedback_matrix[turn][0] + ""


                # Correct colour, incorrect place
                """

        #If guess is correct, end game
        if current_guess == code_to_guess:
            print_instructions()
            print_board(board)
            print " "
            print "CONGRATULATIONS, you guessed the correct code (%s) in %d guesses" % (code_to_guess, turn)
            print " "
            break
            # Write results to file##### - doesn't work

            score_output.write("James")

        elif turn == 8:
            print_instructions()
            print_board(board)
            print "\n" * 5
            print "Unfortunately you didn't guess it, the correct code was %s" % code_to_guess
            print "\n" * 5

    score_output.close()
whole_game()
play_again = "r"
play_again = raw_input("Press any key to play again or type ctrl + c to exit")
while play_again == "Y" or "y" or "r":
    print "\n" * 50
    whole_game()
