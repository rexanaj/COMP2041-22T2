#!/usr/bin/env python3

"""
Prints a table of multiplications.
"""

import sys


def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} m n width")
        sys.exit(1)

    m = int(sys.argv[1])
    n = int(sys.argv[2])
    width = int(sys.argv[3])

    # Loop through each row
    for i in range(1, m+1):
        # seq = " " * (width-len(str(i)))  # 2 -> "2" -> len("2") = 1
        # print(seq, end="")
        print(f"{i:{width}}", end="")
        for j in range(2, n+1):
            print(f"{i*j:{width}}", end="")
        print()


if __name__ == "__main__":
    main()
