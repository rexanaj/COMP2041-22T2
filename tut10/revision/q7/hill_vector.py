#!/usr/bin/env python3

import sys
from collections import Counter


def main():
    for line in sys.stdin:
        # Turns a line of input into a list of ints
        nums = list(map(int, line.split()))

    if len(nums) < 3:
        print("not hill")
        return

    # Go through and see if ascent, apex, descent are there

    # Check the apex is the maximum and occurs only once
    if nums.count(max(nums)) != 1:
        print("not hill")
        return

    ascent = False
    descent = False

    prev = nums[0]
    for num in nums[1:]:
        if prev < num and descent == False:
            ascent = True
        elif prev > num and ascent == True:
            descent = True
        else:
            # Must be strictly ascending/descending
            print("not hill")
            return
        prev = num

    # after looping through, check ALL conditions are satisfied
    if ascent and descent:
        print("hill")


if __name__ == "__main__":
    main()
