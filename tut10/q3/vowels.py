#!/usr/bin/env python3


"""
Approach 1 (nested for loops)
    - Loop through each line
    - Loop through each character in the line
"""

import sys

VOWELS = "aeiou"
# AEIOU


def main():
    mapping = str.maketrans(VOWELS.lower() + VOWELS.upper(),  # aieouAEIOU
                            VOWELS.upper() + VOWELS.lower())  # AEIOUaeiou

    for line in sys.stdin:
        new_line = line.translate(mapping)
        print(new_line)


if __name__ == "__main__":
    main()
