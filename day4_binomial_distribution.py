"""
The ratio of boys to girls for babies born in Russia is 1.09:1.
If there is 1 child born per birth, what proportion of Russian
families with exactly 6 children will have at least 3 boys?

Write a program to compute the answer using the above parameters.
Then print your result, rounded to a scale of decimal places (i.e., 1.234 format).
"""
boys_ratio = 1.09
girls_ratio = 1.00

# finding boys and girls percentage
boys_percentage = boys_ratio / (boys_ratio + girls_ratio)
girls_percentage = girls_ratio / (boys_ratio + girls_ratio)

# probability of each choice we want, boys
p = boys_percentage
# the number of choices we want, at least 3
klist = [3, 4, 5, 6]
# The total number of choices, 6 children
n = 6


def factorial(num):
    ret = 1
    for i in range(num):
        ret *= num - i
    return ret


def combine_prob(n, r, repeat=False):
    """
    Calculate probability by combination method. For combination, order does not matter.
    :param n: number of types to choose from
    :param r: number of choosing time
    :param repeat: with or without repetition
    :return: probability
    """
    if repeat:
        return factorial(r + n - 1) // factorial(r) * factorial(n - 1)
    else:
        # without repeat, it is similar to permutation without repetition
        # just that the order does not matter.
        return factorial(n) // (factorial(r) * factorial(n - r))

# summary of possibility for for families with at least 3 children
sum_p = 0
for k in klist:
    # finding possibility with bias.
    possibility = (p ** k) * ((1 - p) ** (n - k))
    outcome = combine_prob(n, k)
    sum_p += outcome * possibility

print(round(sum_p, 3))
