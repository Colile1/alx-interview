#!/usr/bin/python3
"""
Solves the N-queens problem and prints all possible solutions.
Handles command-line arguments and error checking.
"""
import sys


def solve_n_queens():
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

    board = [-1] * n
    solutions = []

    def is_safe(row, col):
        """
        Checks if placing a queen at (row, col) is safe.
        A queen is safe if no other queen attacks it horizontally,
        vertically, or diagonally.
        """
        for prev_row in range(row):
            if board[prev_row] == col:
                return False
            if abs(row - prev_row) == abs(col - board[prev_row]):
                return False
        return True

    def backtrack(row):
        """
        Recursive backtracking function to find all solutions.
        """
        if row == n:
            current_solution = []
            for r, c in enumerate(board):
                current_solution.append([r, c])
            solutions.append(current_solution)
            return

        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)

    backtrack(0)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    solve_n_queens()
