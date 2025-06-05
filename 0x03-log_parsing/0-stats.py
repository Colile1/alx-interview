#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.

Input format: <IP Address> -
[<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
After every 10 lines and/or a keyboard interruption (CTRL + C),
this script prints statistics: total file size and counts for each
HTTP status code encountered so far.
Status codes are printed in ascending order.
"""
import sys
import signal
import re

# Global variables to store metrics
total_file_size = 0
status_code_counts = {}
line_counter = 0

LOG_LINE_PATTERN = re.compile(
    r'^\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*-\s*\[(.*?)\]\s*'
    r'"GET /projects/260 HTTP/1\.1"\s*(\d+)\s*(\d+)\s*$'
)

# Set of valid HTTP status codes to track
VALID_STATUS_CODES = {200, 301, 400, 401, 403, 404, 405, 500}


def print_statistics():
    """
    Prints the accumulated statistics: total file size
    and counts per status code.
    Status codes are printed in ascending order.
    """
    sys.stdout.write("File size: {}\n".format(total_file_size))
    sorted_codes = sorted(status_code_counts.keys())
    for code in sorted_codes:
        if status_code_counts[code] > 0:
            sys.stdout.write("{}: {}\n".format(code, status_code_counts[code]))
    sys.stdout.flush()


def signal_interrupt_handler(sig, frame):
    """
    Handles keyboard interruption (CTRL+C).
    Prints the current statistics and then allows the script to terminate,
    which will typically show a KeyboardInterrupt traceback from the main loop.
    """
    print_statistics()
    """
    # The KeyboardInterrupt exception will be raised in the main thread
    # after this handler returns, typically from the interrupted I/O operation.
    # This allows the try/except block in the main execution flow to handle it
    # and produce the desired traceback.
    # Forcing an exit here with sys.exit() would prevent that specific
    # Raising KeyboardInterrupt directly here would also work but might change
    # the origin of the traceback slightly. Standard behavior is preferred.
    """


signal.signal(signal.SIGINT, signal_interrupt_handler)

try:
    for line in sys.stdin:
        line_counter += 1
        processed_line = line.strip()

        match = LOG_LINE_PATTERN.match(processed_line)

        if match:
            try:
                """
                # ip_address = match.group(1)
                Captured but not used for current stats
                # date_info = match.group(2)
                Captured but not used for current stats
                """
                status_code_str = match.group(3)
                file_size_str = match.group(4)

                current_file_size = int(file_size_str)
                current_status_code = int(status_code_str)

                total_file_size += current_file_size

                if current_status_code in VALID_STATUS_CODES:
                    status_code_counts[current_status_code] = \
                        status_code_counts.get(current_status_code, 0) + 1
            except ValueError:
                """
                This handles cases where int() conversion might fail,
                though the regex (d+) makes this unlikely for
                status_code & file_size
                if they are purely numeric. Lines that cause this are
                effectively skipped.
                """
                pass
        """
        Lines not matching LOG_LINE_PATTERN are skipped as per requirements.
        """

        if line_counter % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    """
    This block catches the KeyboardInterrupt that propagates after the
    signal_interrupt_handler has run (or if CTRL+C occurs elsewhere).
    The handler should have already printed the stats.
    Re-raising it ensures the script terminates with the standard traceback,
    as shown in the project example.
    """
    raise
finally:
    """
    No final print here, as per the problem's specific conditions for printing:
    "After every 10 lines and/or a keyboard interruption".
    If a final print on EOF regardless of line count was desired,
    it would be added here, taking care not to double-print on CTRL+C.
    """
    pass
