#!/usr/bin/env python3

"""
Given the URL of a web page, fetches it by using the `requests` and the 
`beautifulsoup4` modules
"""

from argparse import ArgumentParser
from collections import Counter

import requests
from bs4 import BeautifulSoup


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "-f", help="Print in order of frequency", action="store_true")
    parser.add_argument("url", help="The URL to be parsed")
    args = parser.parse_args()

    response = requests.get(args.url)
    webpage = response.text

    # Use beautiful soup to grab the tags
    soup = BeautifulSoup(webpage, 'html5lib')
    tags = soup.find_all()
    names = [tag.name for tag in tags]

    counts = Counter()
    for name in names:
        counts[name] += 1

    if args.f:
        # Print out the tags with the frequency in ascending order
        for tag, count in reversed(counts.most_common()):
            print(f"{tag} {count}")
    else:
        # Print out the tags in alphabetical order
        for tag in sorted(counts.keys()):
            print(f"{tag} {counts[tag]}")


if __name__ == "__main__":
    main()
