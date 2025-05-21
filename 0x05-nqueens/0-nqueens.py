#!/usr/bin/python3
"""
Solves the N queens problem.
"""
import sys


def solve_nqueens(N):
    def backtrack(row, queens, diagonals, anti_diagonals, cols):
        if row == N:
            result.append([[i, queens[i]] for i in range(N)])
            return

        for col in range(N):
            curr_diagonal = row - col
            curr_anti_diagonal = row + col
            
            if (col not in cols and 
                curr_diagonal not in diagonals and 
                curr_anti_diagonal not in anti_diagonals):
                
                queens[row] = col
                cols.add(col)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)
                
                backtrack(row + 1, queens, diagonals, anti_diagonals, cols)
                
                cols.remove(col)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)

    result = []
    queens = [0] * N
    backtrack(0, queens, set(), set(), set())
    return result


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)


if __name__ == '__main__':
    main()