"""
PROBLEM 5

Write a program to calculate the sum of series up to n term.

For example, if n = 5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
"""

def cal_sum(n):
    term = 0
    tsum = 0
    for i in range(n):
        term = term * 10 + 2
        tsum += term
    return tsum

# Test Case 1
n1 = 5
print("Output:", cal_sum(n1))

# Test Case 2
n2 = 6
print("Output:", cal_sum(n2))