"""
Day 0: Mean, Median and Mode.

Mean = summary of all inputs divided by number of inputs.
Median = inputs are sorted in ascending or descending manner and the 2 middle values are averaged.
Mode = find value with maximum occurrence count, smallest value is favored.
"""
import math
from itertools import groupby
from sys import stdin


def frm_float(n):
    return '{:.1f}'.format(n)


def frm_int(n):
    return '{:.0f}'.format(n)


def mean(a, c):
    return frm_float(sum(a) / c)


def median(a, c):
    s = sorted(a)
    mid = math.ceil(c / 2) - 1  # minus 1 to change it to zero-based number for array index
    # Example for finding median in array
    # If input count = 10, then mid is 4 ((10 / 2) - 1)
    # idx 0   1   2   3  [4   5]  6   7   8   9
    # val a   b   c   d  [e   f]  g   h   i   j
    #                     ^   ^
    #                   mid   mid + 2
    return frm_float(sum(s[mid: mid + 2]) / 2)


def mode(a):
    s = sorted(a)
    return frm_int(max([[key, len(list(group))] for key, group in groupby(s)], key=lambda x: x[1])[0])

# Read input here
input_count = int(stdin.readline())
inputs = stdin.readline()

input_array = [int(x) for x in inputs.split(' ')]  # split inputs into array

print(mean(input_array, input_count))  # print mean
print(median(input_array, input_count))  # print median
print(mode(input_array))  # print mode
