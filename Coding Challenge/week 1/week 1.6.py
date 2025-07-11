"""
PROBLEM 6

Write a program to Reverse below given numbers without slicing

Test Case 1:

Input: 745633
Output: 336547

Test Case 2:

Input: 65346
Output: 64356
"""

def rev_numb(num):
    rev_num = 0
    while num > 0:
        digit = num % 10  # Extract last digit
        rev_num = rev_num * 10 + digit  # Append digit to rev_num
        num //= 10  # Remove last digit from number
    return rev_num

# Test Case 1
in1 = 745633
print("Output:", rev_numb(in1))

# Test Case 2
in2 = 65346
print("Output:", rev_numb(in2))