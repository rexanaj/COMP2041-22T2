#!/usr/bin/env python3

import sys
from re import compile


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} [lineNo | regex]")
        sys.exit(1)

    try:
        match = int(sys.argv[1])
    except ValueError:
        match = compile(sys.argv[1][1:-1])

    for line_num, line in enumerate(sys.stdin, start=1):
        print(line, end='')

        if isinstance(match, int):
            if line_num == match:
                return
        else:
            # Regex
            if match.search(line):
                return


if __name__ == "__main__":
    main()
