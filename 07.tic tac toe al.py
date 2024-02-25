import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_player_move(board):
    while True:
        move = input("Enter your move (row column): ")
        try:
            row, col = map(int, move.split())
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter row and column numbers.")

def get_ai_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            return row, col

def play_tic_tac_toe():
    board = [[' ']*3 for _ in range(3)]

    print("Welcome to Tic-Tac-Toe!")

    while True:
        print_board(board)
        player_row, player_col = get_player_move(board)
        board[player_row][player_col] = 'X'

        if check_winner(board, 'X'):
            print_board(board)
            print("Congratulations! You win!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        print_board(board)
        ai_row, ai_col = get_ai_move(board)
        print("AI's move:", ai_row, ai_col)
        board[ai_row][ai_col] = 'O'

        if check_winner(board, 'O'):
            print_board(board)
            print("Sorry, AI wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()
