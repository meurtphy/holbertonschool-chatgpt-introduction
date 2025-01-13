#!/usr/bin/python3

def print_board(board):
    """
    Display the current state of the board.
    """
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:  # Avoid printing separator after the last row
            print("-" * 5)

def check_winner(board):
    """
    Check if there is a winner in the current board state.

    Returns:
        str: The winning player's symbol ('X' or 'O'), or None if no winner.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None  # No winner

def is_draw(board):
    """
    Check if the board is full and no winner is found.

    Returns:
        bool: True if the board is full and there is no winner, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main function to play the Tic-Tac-Toe game.
    """
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)


        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {current_player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {current_player}: "))
            if row not in range(3) or col not in range(3):
                print("Invalid input. Row and column must be 0, 1, or 2.")
                continue
        except ValueError:
            print("Invalid input. Please enter numeric values only.")
            continue


        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue


        board[row][col] = current_player


        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break


        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break


        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()
