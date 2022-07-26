#!/usr/bin/env python3

"""
Given the URL of a web page, fetches it by running `wget` and prints the HTML
tags it uses. 
Added a `-f` tag to sort by frequency.
"""
import sys
import subprocess
import re
from argparse import ArgumentParser
from collections import Counter


def main():

    # Another way of parsing commandline arguments
    parser = ArgumentParser()
    parser.add_argument(
        "-f", help="Print in order of frequency", action="store_true")
    parser.add_argument("url", help="The URL to be parsed")
    args = parser.parse_args()

    # By default, subprocess.run captures a bytes-like object --> Make sure to use
    # text=True
    process = subprocess.run(
        f"wget -q -O- {args.url}", capture_output=True, shell=True, text=True)
    webpage = process.stdout

    counts = Counter()
    for tag in re.findall(r'<([a-z]+).*?>', webpage):
        counts[tag] += 1

    if args.f:
        # Print out the tags with the frequency in ascending order
        for tag, count in reversed(counts.most_common()):
            print(f"{tag} {count}")

        # Can't use this, values aren't unique and we can't find the key based
        # on the value
        # for tag, count in reversed(counts.values()):
        #     print(f"{tag} {count}")
    else:
        # Print out the tags in alphabetical order
        for tag in sorted(counts.keys()):
            print(f"{tag} {counts[tag]}")


if __name__ == "__main__":
    main()
