#!/usr/bin/python3
"""
Prime Game: Maria and Ben take turns picking primes and removing them and their multiples.
"""

def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    n = max(nums)
    # Sieve of Eratosthenes to count primes up to n
    is_prime = [True for _ in range(n + 1)]
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    # Count primes up to each i
    primes_count = [0] * (n + 1)
    count = 0
    for i in range(n + 1):
        if is_prime[i]:
            count += 1
        primes_count[i] = count

    maria_wins = 0
    ben_wins = 0
    for num in nums:
        if primes_count[num] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
