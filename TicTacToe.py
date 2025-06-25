import random
tic=[[0,0,0],[0,0,0],[0,0,0]]


def print_board():
    for i in range(3):
        for j in range(3):
            if tic[i][j] == 0:
                print("_", end=" ")
            elif tic[i][j] == 1:
                print("X", end=" ")
            else:
                print("O", end=" ")
        print()
    print()


def check_winner():
    for i in range(3):
        if tic[i][0] == tic[i][1] == tic[i][2] != 0:
            return tic[i][0]
        if tic[0][i] == tic[1][i] == tic[2][i] != 0:
            return tic[0][i]
    if tic[0][0] == tic[1][1] == tic[2][2] != 0:
        return tic[0][0]
    if tic[0][2] == tic[1][1] == tic[2][0] != 0:
        return tic[0][2]
    return 0

def is_full():
    for i in range(3):
        for j in range(3):
            if tic[i][j] == 0:
                return False
    return True

def play_game():
    print("Welcome to Tic Tac Toe!")
    print("Player 1 is X and Player 2 is O")
    print_board()
    player = 1
    while True:
        row = int(input(f"Player {player}, enter the row (0-2): "))
        col = int(input(f"Player {player}, enter the column (0-2): "))
        if tic[row][col] == 0:
            tic[row][col] = player
            print_board()
            winner = check_winner()
            if winner != 0:
                print(f"Player {winner} wins!")
                break
            if is_full():
                print("It's a draw!")
                break
            player = 3 - player
        else:
            print("Invalid move, try again.")

play_game()