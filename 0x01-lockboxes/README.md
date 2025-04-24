# 0x01. Lockboxes

## Description
This project contains a solution to the classic lockboxes problem. The goal is to determine if all boxes in a sequence can be opened, given that each box may contain keys to other boxes. The first box (box 0) is always unlocked, and you must use the keys found in each box to open as many boxes as possible.

## Problem Statement
You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.

- A key with the same number as a box opens that box.
- You can assume all keys will be positive integers.
- There can be keys that do not have boxes.
- The first box `boxes[0]` is unlocked.
- Return `True` if all boxes can be opened, else return `False`.

## Files
- `0-lockboxes.py`: Contains the function `canUnlockAll(boxes)` that implements the solution.

## Usage
To use the function, import it and pass a list of lists representing the boxes and their keys:

```
#!/usr/bin/python3
canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False
```

## Implementation Details
- The solution uses a Depth-First Search (DFS) approach to traverse the boxes using the keys found.
- A set is used to keep track of opened boxes to avoid revisiting.
- The algorithm ensures efficient traversal and checks if all boxes can be opened.

## Requirements
- Python 3.4+
- All files should be executable and follow PEP 8 style.
