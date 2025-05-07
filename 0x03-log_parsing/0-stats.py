#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
"""
import sys
import re


def print_statistics(total_file_size, status_codes_counts):
    """Prints the aggregated statistics.

    Args:
        total_file_size (int): The total size of files processed.
        status_codes_counts (dict): A dictionary with status codes as keys
                                     and their counts as values.
    """
    print("File size: {}".format(total_file_size))
    sorted_codes = sorted(status_codes_counts.keys())
    for code in sorted_codes:
        if status_codes_counts[code] > 0:
            print("{}: {}".format(code, status_codes_counts[code]))


if __name__ == "__main__":
    total_file_size = 0
    status_codes_counts = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }
    line_count = 0

    log_pattern = re.compile(
        r'^\s*(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*-\s*'
        r'\[(?P<date>.*?)\]\s*'
        r'"GET /projects/260 HTTP/1\.1"\s*'
        r'(?P<status_code>\d{3})\s*'
        r'(?P<file_size>\d+)\s*$'
    )

    try:
        for line in sys.stdin:
            line = line.strip()
            match = log_pattern.match(line)

            if match:
                data = match.groupdict()
                try:
                    status_code = int(data['status_code'])
                    file_size = int(data['file_size'])

                    # Aggregate file size
                    total_file_size += file_size

                    # Aggregate status codes
                    if status_code in status_codes_counts:
                        status_codes_counts[status_code] += 1
                    line_count += 1

                except ValueError:
                    pass

            else:
                pass

            if line_count % 10 == 0 and line_count > 0:
                print_statistics(total_file_size, status_codes_counts)

    except KeyboardInterrupt:
        print_statistics(total_file_size, status_codes_counts)
        raise
    finally:
        pass
