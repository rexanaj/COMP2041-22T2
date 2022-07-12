#!/usr/bin/env python3

import sys

num_lines = 10

# Check if `-n` option was provided
if len(sys.argv) >= 2 and sys.argv[1].startswith('-'):
    num_lines = int(sys.argv[1][1:])

counter = 0
for line in sys.stdin:
    # print(line)  # By default, appends a newline to the string
    # print(line, end='')  # Prints without a newline
    if counter >= num_lines:
        break
    sys.stdout.write(line)
    counter += 1
