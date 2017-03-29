"""
A random variable, X, follows Poisson distribution with mean of 2.5.
Find the probability with which the random variable X is equal to 5.
"""


def factorial(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret

# logarithm
e = 2.71828

# average number of success
lamb = 2.5

# actual number of successes that occur
k = 5

ans = (lamb ** k) * (e ** (-1 * lamb)) / factorial(k)

print(round(ans, 3))
