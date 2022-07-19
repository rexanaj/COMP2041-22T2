#!/usr/bin/env python3

"""
Prints the number of lines of C source code in the current directory
Works like `wc -l *.[ch]`
"""

from glob import glob


def main():
    total = 0
    for filename in sorted(glob("*.[ch]")):
        with open(filename) as f:
            lines = f.readlines()
            num_lines = len(lines)
            print(f"{num_lines:8} {filename}")
            total += num_lines
    print(f"{total:8} total")


if __name__ == "__main__":
    main()
