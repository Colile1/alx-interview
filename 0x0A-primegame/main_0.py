#!/usr/bin/python3
"""
Test for Prime Game
"""
isWinner = __import__('0-prime_game').isWinner

if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
