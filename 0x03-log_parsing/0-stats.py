#!/usr/bin/python3
import sys
import re


def print_statistics(total_size, status_codes):
    """Prints the accumulated statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


total_file_size = 0
status_codes = {
    200: 0, 301: 0, 400: 0, 401: 0,
    403: 0, 404: 0, 405: 0, 500: 0
}
line_count = 0

log_pattern = re.compile(
    r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '
    r'\[(.*?)\] "GET /projects/260 HTTP/1.1" '
    r'(\d+) (\d+)'
)

try:
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)

        if not match:
            continue
        try:
            status_code = int(match.group(3))
            file_size = int(match.group(4))

            total_file_size += file_size

            if status_code in status_codes:
                status_codes[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_statistics(total_file_size, status_codes)

        except ValueError:
            pass


except KeyboardInterrupt:
    pass  # Statistics are printed in the finally block


finally:
    print_statistics(total_file_size, status_codes)
