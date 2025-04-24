#!/usr/bin/python3
"""
Module for checking if all lockboxes can be opened.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of list of int): List of boxes with keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    opened = set([0])
    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if 0 <= key < n and key not in opened:
                opened.add(key)
                stack.append(key)
    return len(opened) == n
