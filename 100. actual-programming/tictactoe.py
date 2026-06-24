import random

# Make a list with 9 spaces.
# This represents the tic-tac-toe board.
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


# Function to print the board
def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


# Function to see if someone has won
def check_winner(player):
    # Rows
    if board[0] == player and board[1] == player and board[2] == player:
        return True
    if board[3] == player and board[4] == player and board[5] == player:
        return True
    if board[6] == player and board[7] == player and board[8] == player:
        return True

    # Columns
    if board[0] == player and board[3] == player and board[6] == player:
        return True
    if board[1] == player and board[4] == player and board[7] == player:
        return True
    if board[2] == player and board[5] == player and board[8] == player:
        return True

    # Diagonals
    if board[0] == player and board[4] == player and board[8] == player:
        return True
    if board[2] == player and board[4] == player and board[6] == player:
        return True

    return False


# Play 9 turns at most
for turn in range(9):

    print_board()

    # Player's turn
    if turn % 2 == 0:

        move = int(input("Choose a spot (1-9): ")) - 1

        while board[move] != " ":
            move = int(input("That spot is taken. Try again: ")) - 1

        board[move] = "X"

        if check_winner("X"):
            print_board()
            print("You win!")
            break

    # Computer's turn
    else:

        # Make a list of empty spots
        empty_spots = []

        for i in range(9):
            if board[i] == " ":
                empty_spots.append(i)

        # Pick one at random
        computer_move = random.choice(empty_spots)

        board[computer_move] = "O"

        print("Computer chose spot", computer_move + 1)

        if check_winner("O"):
            print_board()
            print("Computer wins!")
            break

# If no one won after 9 turns
else:
    print_board()
    print("It's a tie!")
