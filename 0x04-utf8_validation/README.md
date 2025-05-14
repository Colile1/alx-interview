# 0x04-utf8_validation

This project contains a Python function to validate whether a given data set represents a valid UTF-8 encoding.

## Files
- `0-validate_utf8.py`: Contains the `validUTF8` function that checks if a list of integers is a valid UTF-8 encoding.

## Usage
Import the `validUTF8` function and pass a list of integers (each representing a byte) to check if it is a valid UTF-8 encoding.

Example:
```python
from 0-validate_utf8 import validUTF8

data = [65]
print(validUTF8(data))  # Output: True
```

## Requirements
- Python 3.4.3+
- All files are executable and PEP 8 compliant.

## Author
- Project for ALX Interview Preparation
