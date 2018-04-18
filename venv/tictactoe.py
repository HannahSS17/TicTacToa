# Tic Tac Toe game

import random


# print the board ( not a list but actual representation of the board )
def display_board(board):
        print("\n"*100)
        print(board[1], " | ", board[2], " | ",  board[3])
        print("--------------")
        print(board[4], " | ", board[5], " | ", board[6])
        print("--------------")
        print(board[7], " | ", board[8], " | ", board[9])


# function assign player input to marker X or O
def player_input():
    marker = ""

    # ask player 1 to choose X or O
    while marker != "X" and marker != "O":
        marker = input("Player 1, choose X or O: ").upper()

    # assign the opposite marker for player 2
    if marker == "O":
       return ("O", "X")
    else:
        return ("X", "O")


# place marker on the board
def place_marker(board, marker, position):
    board[position] = marker

# check if theres a win or a tie

def win_check(board, mark):

    # all rows, columns + diagonals have the same marker
    return ( (board[1] ==  board[2] == board[3] == mark) or # horizonal
    (board[4] == board[5] == board[6] == mark) or # horizonal
    (board[7] == board[8] == board[9] == mark) or # horizonal
    (board[1] == board[4] == board[7] == mark) or # vertical
    (board[2] == board[5] == board[8] == mark) or # vertical
    (board[3] == board[6] == board[9] == mark) or # vertical
    (board[1] == board[5] == board[9] == mark) or # diagonal
    (board[3] == board[5] == board[7] == mark) ) # diagonal


# randomly decide which player starts the game

def choose_first():
    flip = random.randint(0,1)

    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"

# check if board position is available to put there the marker

def space_check(board, position):

    return board[position] == " "

# check if the board is full

def full_board_check(board):

    for i in range(1, 10):
        if space_check(board, i):
            return False
    # board is full if we return True
    return True

# ask player for the next position

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Choose position: (1-9) "))
    return position

# ask for replay the game or not

def replay():

    choice =  input("Play again?   y or n ")

    return choice == "y"


################################

# while loop to keep running the game
print("Welcome to Tic Tac Toe")

while True:
    # Play the game

    # set everything up (board, who is first, choose markers: X, O)
    the_board = [" "]*10
    player1_marker, player2_marker = player_input()


    turn = choose_first()
    print(turn , " will go first")

    play_game = input("Ready to play? y or n ")

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    # Game play
    while game_on:

        if turn == "Player 1":

            # PLAYER 1 TURN

            # show the board
            display_board(the_board)
            # choose the position
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board, player1_marker, position)

            # check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Player 1 has won!")
                game_on = False
            # check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie game")
                    game_on = False
                else:
                    turn = "Player 2"

            # PLAYER 2 TURN

        else:
            # show the board
            display_board(the_board)
            # choose the position
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board, player2_marker, position)

            # check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("Player 2 has won!")
                game_on = False
            # check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie game")
                    game_on = False
                else:
                    turn = "Player 1"

    # break out of the while loop on replay()
    if not replay():
        break


