#!/usr/bin/env python3

"""
Given the URL of a web page, fetches it by running `wget` and prints the HTML
tags it uses

wget -q -O- https://www.cse.unsw.edu.au
"""

import sys
import subprocess
import re
from collections import Counter


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <url>")
        sys.exit(0)

    url = sys.argv[1]
    # By default, subprocess.run captures a bytes-like object --> Make sure to use
    # text=True
    process = subprocess.run(
        f"wget -q -O- {url}", capture_output=True, shell=True, text=True)
    webpage = process.stdout

    # DO WANT:      Open tag: <div>
    # DON'T WANT:   HTML comment: <!-- This is my comment -->
    # DON'T WANT:   Closing tag: </ div>

    counts = Counter()
    # counts = {}   # Counter() is the same as {} but has a default value of 0

    # Regex suggestion: <[^/!].*>
    # for tag in re.findall(r'<[^/!][^>]+>', webpage):  Another way to grab tags
    for tag in re.findall(r'<([a-z]+).*?>', webpage):
        counts[tag] += 1

    # Can also use sorted() on a list of tuples
    # for tag, count in sorted(counts.items()):
    #     print(f"{tag} {count}")

    # Print out the tags in alphabetical order
    for tag in sorted(counts.keys()):
        print(f"{tag} {counts[tag]}")


if __name__ == "__main__":
    main()
