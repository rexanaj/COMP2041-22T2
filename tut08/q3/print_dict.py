#!/usr/bin/env python3

"""
Displays the contents of a dict in the format below:
    [key] => value
    [Andrew] => green
    [Anne] => red
    [John] => blue
"""

dictionary = {
    "Andrew": "green",
    "key": "value",
    "John": "blue",
    "Anne": "red",
}


def print_dict(d):
    for key, value in d.items():
        # print(key, value)
        print(f"[{key}] => {value}")

    # for i in d.keys():
    # print(i)
    # print(d.keys())


if __name__ == "__main__":
    print_dict(dictionary)
