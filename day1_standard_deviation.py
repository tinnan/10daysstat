"""
Given an array, X, of N integers, calculate and print the standard deviation. Your answer should be in decimal form,
rounded to a scale of 1 decimal place (i.e., 12.3 format). An error margin of +-0.1 will be tolerated for the standard deviation.
"""
import math


def mean(a, c):
    return sum(a) / c

count = int(input())
inputs = [int(x) for x in input().split(' ')]

m = mean(inputs, count)
# calculate variance
v = sum([(i - m) ** 2 for i in inputs]) / count
# calculate standard deviation
s = math.sqrt(v)

print('{:.1f}'.format(s))
