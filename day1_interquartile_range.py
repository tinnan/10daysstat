"""
The inter quartile range of an array is the difference between its first (Q1) and third (Q3) quartiles (i.e., Q3 - Q1).

Given an array, X, of  integers and an array, F, representing the respective frequencies of X's elements, construct
a data set, S, where each x occurs at frequency f. Then calculate and print S's interquartile range, rounded to a
scale of 1 decimal place (i.e., 12.3 format).
"""
import math


def median(a, c):
    mid = math.ceil(c / 2) - 1  # minus 1 to change it to zero-based number for array index
    # Example for finding median in array
    # If input count = 10, then mid is 4 ((10 / 2) - 1)
    # idx 0   1   2   3  [4   5]  6   7   8   9
    # val a   b   c   d  [e   f]  g   h   i   j
    #                     ^   ^
    #                   mid   mid + 2
    if c % 2 == 1:
        # when count is an even number, return middle value
        return a[mid]
    return sum(a[mid: mid + 2]) / 2


count = int(input())
inputs = [int(e) for e in input().split(' ')]
freq = [int(e) for e in input().split(' ')]

# construct data set
dataset = []
for idx in range(count):
    i = inputs[idx]
    for j in range(freq[idx]):
        dataset.append(i)

dataset = sorted(dataset)

set_count = len(dataset)
if set_count % 2 == 0:
    # even input count
    m = set_count // 2
    low = dataset[0:m]
    high = dataset[m:]
else:
    # odd input count
    m = math.ceil(set_count / 2)
    low = dataset[0:m - 1]
    high = dataset[m:]

q1 = median(low, len(low))
q3 = median(high, len(high))

inter_quartile = q3 - q1
print('{:.1f}'.format(inter_quartile))
