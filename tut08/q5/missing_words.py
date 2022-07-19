#!/usr/bin/env python3

"""
Given two files as arguments prints, in sorted order, all the words found in 
file1 but not file2.
"""
import sys


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} file1 file2")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    # Grab the words in file1
    file1_words = set()
    with open(file1) as f1:
        for line in f1:
            file1_words.add(line.strip())

    file2_words = set()
    with open(file2) as f2:
        for line in f2:
            file2_words.add(line.strip())

    # Find the difference between file1_words and file2_words
    # Can also use `file1_words.difference(file2_words)`
    for word in sorted(file1_words - file2_words):
        print(word)


if __name__ == "__main__":
    main()
