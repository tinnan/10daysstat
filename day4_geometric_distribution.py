"""
The probability that a machine produces a defective product is 1/3.
What is the probability that the 1st defect is found during the 5th inspection?
"""

# Formula success rate a.k.a product defective rate
p = 1/3
# Formula failure rate
q = 1 - p

# Total number of binomial experiment
n = 5

ans = (q ** (n - 1)) * p

print(round(ans, 3))
