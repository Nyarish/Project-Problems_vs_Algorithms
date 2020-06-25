#!/usr/bin/env python
# coding: utf-8

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return (None, None)

    min_val = ints[0]
    max_val = ints[0]

    for num in ints:
        # If minval is greater than current element, then update minval
        if min_val > num:
            min_val = num

        # If maxval is less than current element, then update maxval
        if max_val < num:
            max_val = num

    return (min_val, max_val)


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print('Test 1')
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print()

print('Test 2: Edge cases')
print("Pass" if ((2, 2) == get_min_max([2])) else "Fail")
print("Pass" if ((-1, 1) == get_min_max([1, -1])) else "Fail")
print()
print('Test 3: Edge cases')
print("Pass" if ((None, None) == get_min_max([])) else "Fail")





