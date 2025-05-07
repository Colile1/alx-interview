# 0x03. Log Parsing

This project contains a script that reads stdin line by line and computes metrics for log entries in a specific format.

## Usage

The script `0-stats.py` reads from standard input and prints statistics after every 10 lines and/or on keyboard interruption (CTRL + C).

### Input format
```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

### Output
- Total file size: sum of all file sizes
- Number of lines by status code (200, 301, 400, 401, 403, 404, 405, 500)

## Example
```
cat some_log_file | ./0-stats.py
```

## Requirements
- Python 3.4+
- Executable permissions on the script
