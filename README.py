python
Tic Tac Toe Game (2 Players)
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, diagonals
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

def play_game():
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"
    moves = 0

    while moves < 9:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        if board[row][col] != " ":
            print("Cell already taken! Try again.")
            continue

        board[row][col] = current_player
        moves += 1

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            returncurrent_player = "O" if current_player == "X" else "X"

    print_board(board)
    print("It's a draw!")

play_game()
