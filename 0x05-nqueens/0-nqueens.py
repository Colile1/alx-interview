#!/usr/bin/python3
import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col].
    A queen can be placed if no other queen attacks it
    along the same column or diagonals.
    """
    # Check this column on upper side
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        if board[i] == j:
            return False
        i -= 1
        j += 1
    return True


def solve_n_queens(n, row, board, solutions):
    """
    Recursively finds all possible solutions for the N-queens problem.
    """
    if row == n:
        # All queens are placed, a solution is found
        solution = []
        for r, c in enumerate(board):
            solution.append([r, c])
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col  # Place queen
            solve_n_queens(n, row + 1, board, solutions)
            # No explicit 'unplace' needed as the board list is passed by value
            # effectively creating a new state for each recursive call or
            # the current value will be overwritten in the next iteration.


def main():
    """
    Main function to parse arguments and initiate the N-queens solver.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # board will store the column position of the queen in each row.
    # For example, board[i] = j means a queen is at row i, column j.
    board = [-1] * n  # Initialize board with -1 (no queen placed)
    solutions = []

    solve_n_queens(n, 0, board, solutions)

    for solution in solutions:
        print(solution)


def solve_n_queens(n, row, board, solutions):
    """
    Recursively solves the N-queens problem using backtracking.

    Args:
        n (int): The size of the chessboard.
        row (int): The current row being considered for placing a queen.
        board (list): A list of [row, col] pairs representing the
        placement of queens.
        solutions (list): A list to store all valid board configurations.
    """
    if row == n:
        # All queens have been placed successfully, add this solution
        solutions.append([list(queen) for queen in board])
        return

    for col in range(n):
        if is_safe(row, col, board):
            # Place the queen and move to the next row
            board.append([row, col])
            solve_n_queens(n, row + 1, board, solutions)
            # Backtrack: Remove the queen to try other possibilities
            board.pop()


def is_safe(current_row, current_col, board):
    """
    Checks if placing a queen at (current_row, current_col) is safe.

    Args:
        current_row (int): The row for the potential queen placement.
        current_col (int): The column for the potential queen placement.
        board (list): The current placement of queens.

    Returns:
        bool: True if safe, False otherwise.
    """
    for r, c in board:
        # Check for same column
        if c == current_col:
            return False
        # Check for diagonals (abs(row_diff) == abs(col_diff))
        if abs(r - current_row) == abs(c - current_col):
            return False
    return True


def main():
    """
    Main function to parse arguments and initiate the N-queens solver.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve_n_queens(n, 0, [], solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
