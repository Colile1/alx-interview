#!/usr/bin/python3
"""
Log parsing script for ALX Interview project.
Reads stdin line by line and computes metrics as specified.
"""
import sys
import re

status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
status_count = {code: 0 for code in status_codes}
total_size = 0
line_count = 0

log_pattern = re.compile(
    r'^(\S+) - \[.*\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
    )


def print_stats():
    print(f"File size: {total_size}")
    for code in sorted(status_count.keys()):
        if status_count[code]:
            print(f"{code}: {status_count[code]}")


try:
    for line in sys.stdin:
        match = log_pattern.match(line.strip())
        if match:
            status = match.group(2)
            size = int(match.group(3))
            total_size += size
            if status in status_count:
                status_count[status] += 1
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
print_stats()
