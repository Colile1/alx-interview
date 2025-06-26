# 0x0A. Prime Game

Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

## Task

Write a function `def isWinner(x, nums)` where:
- `x` is the number of rounds.
- `nums` is a list of integers, each representing the maximum number in a round.
- Maria always goes first.
- Both players play optimally.
- Return the name of the player that won the most rounds. If the winner cannot be determined, return `None`.
- You cannot import any packages in this task.

## Example

```
x = 3
nums = [4, 5, 1]

First round: n = 4
Maria picks 2 and removes 2, 4 (leaving 1, 3)
Ben picks 3 and removes 3 (leaving 1)
Ben wins (no primes left for Maria)

Second round: n = 5
Maria picks 2 and removes 2, 4 (leaving 1, 3, 5)
Ben picks 3 and removes 3 (leaving 1, 5)
Maria picks 5 and removes 5 (leaving 1)
Maria wins (no primes left for Ben)

Third round: n = 1
Ben wins (no primes for Maria to choose)

Result: Ben has the most wins.
```

## Usage

```
#!/usr/bin/python3
isWinner = __import__('0-prime_game').isWinner
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
```

## Requirements
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Code should use the PEP 8 style (version 1.7.*)
- Only the standard library is allowed
