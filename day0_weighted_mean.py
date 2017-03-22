"""
Weighted mean.
"""
from sys import stdin


def weighted_mean(n, v, w):
    s_v = 0
    s_w = 0
    for i in range(n):
        s_v += v[i] * w[i]
        s_w += w[i]
    return '{:.1f}'.format(s_v / s_w)


n = int(stdin.readline())  # number of elements
values = [int(v) for v in stdin.readline().split(' ')]  # values
weights = [int(w) for w in stdin.readline().split(' ')]  # weights

print(weighted_mean(n, values, weights))
