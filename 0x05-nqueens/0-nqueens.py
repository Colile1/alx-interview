#!/usr/bin/python3
import sys


def solve_n_queens(n, row, board, solutions):
    """
    Recursively solves the N-queens problem using backtracking.

    Args:
        n (int): The size of the chessboard.
        row (int): The current row being considered for placing a queen.
        board (list): A list of [row, col] pairs representing
        the placement of queens.
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
