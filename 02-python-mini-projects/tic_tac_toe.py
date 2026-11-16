# Tic Tac Toe Game
# A two-player Python game
# Python Bootcamp - Milestone Project 1


# Step 1: Display the Game Board

from IPython.display import clear_output

def display_board(board):

    clear_output()
    
    print(' ','|',' ','|')
    print(board[7],'|',board[8],'|',board[9])
    print(' ','|',' ','|')
    print('---------')
    print(' ','|',' ','|')
    print(board[4],'|',board[5],'|',board[6])
    print(' ','|',' ','|')
    print('---------')
    print(' ','|',' ','|')
    print(board[1],'|',board[2],'|',board[3])
    print(' ','|',' ','|')


# Step 2: Choose Player Markers (X or O)

def player_input():

    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('player 1 please choose X or O ').upper()

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1, player2)


# Step 3: Place a Marker on the Board

def place_marker(board, marker, position):

    board[position] = marker 


# Step 4: Check if a Player Has Won

def win_check(board, mark):

    # Check horizontal rows
    if board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    if board[4] == mark and board[5] == mark and board[6] == mark:
        return True

    # Check vertical columns
    if board[3] == mark and board[6] == mark and board[9] == mark:
        return True 
    if board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    if board[1] == mark and board[4] == mark and board[7] == mark:
        return True

    # Check diagonals
    if board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    if board[1] == mark and board[5] == mark and board[9] == mark:
        return True

    return False


# Step 5: Randomly Choose the Starting Player

import random

def choose_first():

    random_num = random.randint(1,2)

    if random_num == 1:
        return 'Player 1'
    else:
        return 'Player 2'


# Step 6: Check if a Position Is Empty

def space_check(board, position):

    return board[position] == ' '


# Step 7: Check if the Board Is Full

def full_board_check(board):

    for strings in board[1:]:

        if strings == ' ':
            return False

    return True


# Step 8: Get the Current Player's Move

def player_choice(board, turn):

    position = 0

    while True:

        if turn == 'Player 1':
            position = int(input('Player 1, choose a number between 1 to 9: '))
        else:
            position = int(input('Player 2, choose a number between 1 to 9: '))

        # Check if the position is valid and empty
        if 1 <= position <= 9 and board[position] == ' ':
            return position


# Step 9: Ask Players if They Want to Play Again

def replay():

    choice = ''

    while choice not in ['Yes', 'No']:

        choice = input('Do you want to play again? Yes or No: ').capitalize()

        if choice not in ['Yes', 'No']:
            print('Sorry, choose Yes or No!')

    if choice == 'Yes':
        return True
    else:
        return False


# Step 10: Main Game Logic

# Display welcome message
print('Welcome to Tic Tac Toe!')


# Main loop: Start a new game or replay
while True:

    # Set up a new game
    the_board = ['#'] + [' '] * 9

    # Assign X and O to players
    player1_marker, player2_marker = player_input()

    # Randomly select the starting player
    turn = choose_first()

    print(turn + ' will go first!')

    # Start the game
    game_on = True


    # Game loop: Continue until someone wins or the game is a draw
    while game_on:

        # Player 1 Turn
        if turn == 'Player 1':

            # Display current board
            display_board(the_board)

            # Get Player 1's position
            position = player_choice(the_board, turn)

            # Place Player 1's marker
            place_marker(the_board, player1_marker, position)

            # Check if Player 1 wins
            if win_check(the_board, player1_marker):

                display_board(the_board)
                print('Player 1 has won!')
                game_on = False

            # Check if the game is a draw
            elif full_board_check(the_board):

                display_board(the_board)
                print('The game is a draw!')
                game_on = False

            # Switch to Player 2
            else:
                turn = 'Player 2'


        # Player 2 Turn
        else:

            # Display current board
            display_board(the_board)

            # Get Player 2's position
            position = player_choice(the_board, turn)

            # Place Player 2's marker
            place_marker(the_board, player2_marker, position)

            # Check if Player 2 wins
            if win_check(the_board, player2_marker):

                display_board(the_board)
                print('Player 2 has won!')
                game_on = False

            # Check if the game is a draw
            elif full_board_check(the_board):

                display_board(the_board)
                print('The game is a draw!')
                game_on = False

            # Switch to Player 1
            else:
                turn = 'Player 1'


    # Step 11: Replay or Exit the Game

    # Ask if players want another game
    if not replay():
        break
