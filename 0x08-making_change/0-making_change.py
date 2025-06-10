#!/usr/bin/python3
"""
0-making_change.py
This module provides a function to determine the minimum number of coins
needed to make a given amount.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): List of coin denominations (integers > 0).
        total (int): The total amount to make change for.

    Returns:
        int: The minimum number of coins needed, or -1 if not possible.
    """
    if total <= 0:
        return 0
    if not coins:
        return -1
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, total + 1):
            if dp[x - coin] != float('inf'):
                dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[total] if dp[total] != float('inf') else -1
