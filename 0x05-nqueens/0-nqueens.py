#!/usr/bin/python3
"""
Solves the N queens problem.
"""
import sys


def print_usage(msg):
    print(msg)
    sys.exit(1)


def is_safe(row, col, solution):
    for r, c in enumerate(solution):
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True


def solve_nqueens(n, row=0, solution=[], solutions=[]):
    if row == n:
        solutions.append([[r, c] for r, c in enumerate(solution)])
        return
    for col in range(n):
        if is_safe(row, col, solution):
            solve_nqueens(n, row + 1, solution + [col], solutions)
    return solutions


def main():
    if len(sys.argv) != 2:
        print_usage("Usage: nqueens N")
    try:
        n = int(sys.argv[1])
    except ValueError:
        print_usage("N must be a number")
    if n < 4:
        print_usage("N must be at least 4")
    solutions = solve_nqueens(n)
    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    main()
