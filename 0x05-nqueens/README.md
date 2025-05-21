# 0x05-nqueens

This project contains a Python program to solve the N queens puzzle using backtracking.

## Files
- `0-nqueens.py`: Solves the N queens problem for any N ≥ 4. Usage: `./0-nqueens.py N`

## Requirements
- Python 3.4.3+
- All files are executable and PEP 8 compliant.
- Only the `sys` module is used.

## Usage
```
./0-nqueens.py
```

```python

#!/usr/bin/python3
"""
Solves the N queens problem.
"""
import sys


def solve_nqueens(N):
    solutions = [[]]
    for row in range(N):
        solutions = place_queen(row, N, solutions)

    return solutions


def place_queen(row, N, prev_solutions):
    new_solutions = []
    for solution in prev_solutions:
        for col in range(N):
            if is_safe(row, col, solution):
                new_solutions.append(solution + [col])
    return new_solutions


def is_safe(row, col, solution):
    for r, c in enumerate(solution):
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True


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
        print([[i, col] for i, col in enumerate(solution)])


if __name__ == '__main__':
    main()
```