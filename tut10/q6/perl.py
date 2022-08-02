#!/usr/bin/env python3

import sys


def chomp(string):
    if string[-1] == "\n":
        # Check if the last character is a newline
        return string[:-1]
    return string


def qw(string):
    # Converts a string to a list of words
    return string.split()


def die(error_msg):
    print(f"Error: {sys.argv[0]} {error_msg}")
    sys.exit(1)


if __name__ == "__main__":
    print("Hello\n", end='')
    print(chomp("Hello\n"), end='')
    print()
    print(qw("hello this is going ot be split    up     "))
    print(die("Uh oh"))
