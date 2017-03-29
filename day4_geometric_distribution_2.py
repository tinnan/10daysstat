"""
The probability that a machine produces a defective product is 1/3.
What is the probability that the 1st defect is found during the first 5 inspections?
"""

# Formula success rate a.k.a product defective rate
p = 1/3
# Formula failure rate
q = 1 - p

# Total number of binomial experiment
n = 5

# List contains number of trails before success is found
k_list = range(1, n+1)  # running 1 ... n

ans = 0
for k in k_list:
    effort = n - k  # effort required before first success is found, running from n-1 ... 0
    ans += (q ** effort) * p

print(round(ans, 3))
