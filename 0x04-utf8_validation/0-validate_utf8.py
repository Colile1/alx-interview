#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Checks if a list of integers represents a valid UTF-8 encoding.
    Args:
        data (list): List of integers representing bytes.
    Returns:
        bool: True if valid UTF-8, False otherwise.
    """
    n_bytes = 0
    for num in data:
        byte = num & 0xFF
        if n_bytes == 0:
            if (byte >> 5) == 0b110:
                n_bytes = 1
            elif (byte >> 4) == 0b1110:
                n_bytes = 2
            elif (byte >> 3) == 0b11110:
                n_bytes = 3
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            n_bytes -= 1
    return n_bytes == 0
