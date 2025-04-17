# Pascal's Triangle

This module generates Pascal's Triangle up to the nth row.

## Function

### `pascal_triangle(n)`

- **Parameters:**
  - `n` (int): The number of rows of Pascal's triangle to generate.

- **Returns:**
  - A list of lists of integers representing Pascal's triangle.
  - Returns an empty list if `n <= 0`.

## Example Usage

```python
if __name__ == "__main__":
    print(pascal_triangle(5))
```

## Output

```
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
