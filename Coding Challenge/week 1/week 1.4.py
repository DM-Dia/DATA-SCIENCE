"""
PROBLEM 4
Write a program to count the total number of digits in a number using a while loop
"""

def count_digits(number):
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count

in1 = 75869
print("Output:", count_digits(in1))

in2 = 654
print("Output:", count_digits(in2))