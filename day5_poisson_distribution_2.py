"""
The manager of a industrial plant is planning to buy a machine of either type A or type B. For each day’s operation:

* The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88.
  The daily cost of operating C_A = 160 + 40X^2 is .
* The number of repairs, Y, that machine B needs is a Poisson random variable with mean 1.55.
  The daily cost of operating C_B = 128 + 40Y^2 is .
Assume that the repairs take a negligible amount of time and the machines are maintained nightly to ensure that they
operate like new at the start of each day. Find and print the expected daily cost for each machine.
"""
# logarithm
e = 2.71828

# average of A
lamb_A = 0.88
# average of B
lamb_B = 1.55

# Daily cost for A: C_A = 160 + 40X^2
# Daily cost for B: C_B = 128 + 40Y^2
# They are special case for poisson distribution
# E[X^2] = lambda + (lambda ^ 2)

ans_A = 160 + (40 * (lamb_A + (lamb_A ** 2)))
ans_B = 128 + (40 * (lamb_B + (lamb_B ** 2)))
print(round(ans_A, 3))
print(round(ans_B, 3))
