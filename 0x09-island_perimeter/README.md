# 0x09. Island Perimeter

This project contains a function to calculate the perimeter of an island described in a grid (list of lists) of integers.

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- Code should use the PEP 8 style (version 1.7.*)
- Only the standard library is allowed

## Files

- `0-island_perimeter.py`: Contains the `island_perimeter(grid)` function.
- `0-main.py`: Test file for the function.

## Task

Write a function `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`:

- `grid` is a list of list of integers:
  - 0 represents water
  - 1 represents land
  - Each cell is square, with a side length of 1
  - Cells are connected horizontally/vertically (not diagonally).
  - `grid` is rectangular, with width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing).
- The island doesn’t have “lakes” (water inside that isn’t connected to the water around the island).

