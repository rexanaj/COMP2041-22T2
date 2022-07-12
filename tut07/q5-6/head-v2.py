#!/usr/bin/env python3

import sys

num_lines = 10

# Check if `-n` option was provided
if len(sys.argv) >= 2 and sys.argv[1].startswith('-'):
    num_lines = int(sys.argv[1][1:])
    # Removing the option from the commandline argument list
    sys.argv.pop(1)

# Check if we're reading from standard input
if len(sys.argv) == 1:
    sys.argv.append('stdin')

for filename in sys.argv[1:]:
    # # Checks if the filename is an option
    # if filename.startswith('-'):
    #     continue
    print(f"==> {filename} <===")
    # print("==> " + filename + " <===") # Alternative: use string concatenation

    if filename == 'stdin':
        stream = sys.stdin
    else:
        stream = open(filename)

    counter = 0
    for line in stream:
        if counter >= num_lines:
            break
        sys.stdout.write(line)
        counter += 1
