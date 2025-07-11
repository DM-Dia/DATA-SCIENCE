"""
PROBLEM 8

Write a Python program to nd the median of three values.

Test case 1: Input:

Input rst number: 15

Input second number: 26

Input third number: 29

Output : 26

Test case 2: Input:

Input rst number: 10

Input second number: 20

Input third number: 5

Output : 10
"""

def find_median(a, b, c):
    if (a > b and a < c) or (a > c and a < b):
        return a
    elif (b > a and b < c) or (b > c and b < a):
        return b
    else:
        return c

# Test Case 1
print("Output:", find_median(15, 26, 29))

# Test Case 2
print("Output:", find_median(10, 20, 5))