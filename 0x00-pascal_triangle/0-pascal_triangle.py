#!/usr/bin/python3
"""
Module for generating Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        list: A list of lists of integers representing Pascal's triangle.
              Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        for j in range(len(prev_row) - 1):
            new_row.append(prev_row[j] + prev_row[j+1])

        new_row.append(1)
        triangle.append(new_row)

    return triangle


if __name__ == "__main__":
    """
    Helper function to print the triangle in the specified format.
    This part is typically in a separate main file (like 0-main.py)
    but included here for completeness if testing this file directly.
    """
    def print_triangle(triangle):
        """
        Print the triangle
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print("Pascal's Triangle for n = 5:")
    print_triangle(pascal_triangle(5))
    print("\nPascal's Triangle for n = 1:")
    print_triangle(pascal_triangle(1))
    print("\nPascal's Triangle for n = 0:")
    print_triangle(pascal_triangle(0))
    print("\nPascal's Triangle for n = -2:")
    print_triangle(pascal_triangle(-2))
