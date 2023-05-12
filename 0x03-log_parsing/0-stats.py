#!/usr/bin/python3
"""Log Parsing Script"""


import sys
import re


# Regular expression to match the input format
regex = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)'

# Initialize metrics
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

# Read from stdin line by line
lines_read = 0

for line in sys.stdin:
    # Parse the line using regular expression
    match = re.match(regex, line.strip())

    if match:
        # Extract the relevant fields
        status_code = int(match.group(3))
        file_size = int(match.group(4))
        
        # Update metrics
        total_size += file_size
        status_codes[status_code] += 1

    # Increment the line count
    lines_read += 1

    # Check if we need to print the statistics
    if lines_read % 10 == 0:
        print('Total file size: File size: {}'.format(total_size))
        for code in sorted(status_codes.keys()):
            if status_codes[code] > 0:
                print('{}: {}'.format(code, status_codes[code]))

    # Check for keyboard interruption
    try:
        if sys.stdin.isatty() and sys.stdin.peek() == '':
            break

    except KeyboardInterrupt:
        print('Total file size: File size: {}'.format(total_size))
        for code in sorted(status_codes.keys()):
            if status_codes[code] > 0:
                print('{}: {}'.format(code, status_codes[code]))
        break
