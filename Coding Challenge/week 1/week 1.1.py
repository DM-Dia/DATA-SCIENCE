"""
PROBLEM 1:
Read an integer N. For all non-negative integers i < N, print i^2.
"""

def print_squares(n):
    squares = [i ** 2 for i in range(n)]
    print(squares)

# Test Case 1
print("Case 1:")
print_squares(5)

#print_squares(10)