"""
A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because
they are incorrectly sized. What is the probability that a batch of 10 pistons will contain:

1. No more than 2 rejects?
2. At least 2 rejects?
"""


def bias(p, n, k):
    """
    biased possibility
    :param p: possibility of interest
    :param n: number of all choice
    :param k: number of choice of interest
    :return:
    """
    return (p ** k) * ((1 - p) ** (n - k))


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


# possibility of rejection
p = 0.12

# number of piston in a batch
n = 10

# Question 1: No more than 2 reject
k_q1_list = [i for i in range(3)]

# Question 2: At least 2 reject
k_q2_list = [i for i in range(2, 11)]


# Question 1 calculation
q1_ans = 0
for k_q1 in k_q1_list:
    q1_ans += bias(p, n, k_q1) * combine_prob(n, k_q1)

# Question 2 calculation
q2_ans = 0
for k_q2 in k_q2_list:
    q2_ans += bias(p, n, k_q2) * combine_prob(n, k_q2)

print(round(q1_ans, 3))
print(round(q2_ans, 3))
