"""
Finding quartiles for the given inputs
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
    return sum(a[mid: mid + 2]) // 2


count = int(input())
inputs = sorted([int(e) for e in input().split(' ')])

if count % 2 == 0:
    # even input count
    m = count // 2
    low = inputs[0:m]
    high = inputs[m:]
else:
    # odd input count
    m = math.ceil(count / 2)
    low = inputs[0:m - 1]
    high = inputs[m:]

q1 = median(low, len(low))
q2 = median(inputs, count)
q3 = median(high, len(high))

print(q1)
print(q2)
print(q3)
