# 0x02. Minimum Operations

## Description
This project provides a solution to the "Minimum Operations" problem. The objective is to determine the fewest number of operations required to achieve exactly `n` 'H' characters in a text file, starting with a single 'H', using only two operations: "Copy All" and "Paste".

## Problem Statement
Given a number `n`, write a method that calculates the minimum number of operations needed to result in exactly `n` 'H' characters in the file.

- Only two operations are allowed: "Copy All" and "Paste".
- The first character is always a single 'H'.
- If `n` is impossible to achieve, return 0.

## Files
- `0-minoperations.py`: Contains the function `minOperations(n)` that implements the solution.

## Usage
To use the function, import it and pass the target number of characters:

```
#!/usr/bin/python3
minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
```

## Implementation Details
- The solution uses a mathematical approach based on prime factorization.
- For each factor of `n`, the factor is added to the operation count, simulating the optimal sequence of "Copy All" and "Paste" operations.
- The algorithm is efficient and ensures the minimum number of operations is found.

## Requirements
- Python 3.4+
- All files should be executable and follow PEP 8 style.

