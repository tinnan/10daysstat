num_of_card = 52


def factorial(num):
    ret = 1
    for i in range(num):
        ret *= num - i
    return ret


def permute_prob(n, r, repeat=False):
    """
    Calculate probability by permutation method. For permutation, order does matter.
    :param n: number of types to choose from
    :param r: number of choosing time
    :param repeat: with or without repetition
    :return: probability in fraction format as array
    """
    if repeat:
        # repeatable permutation
        return n ** r
    else:
        return factorial(n) // factorial(n - r)

print(permute_prob(11, 3, True))


def combine_prob(n, r, repeat=False):
    """
    Calculate probability by combination method. For combination, order does not matter.
    :param n: number of types to choose from
    :param r: number of choosing time
    :param repeat: with or without repetition
    :return: probability
    """
    if repeat:
        return [factorial(r + n - 1), factorial(r) * factorial(n - 1)]
    else:
        # without repeat, it is similar to permutation without repetition
        # just that the order does not matter.
        return factorial(n) // (factorial(r) * factorial(n - r))


# print(combine_prob(13, 2))
# print(combine_prob(52, 2))
#
# print(combine_prob(7, 3))
# print(combine_prob(6, 4))
