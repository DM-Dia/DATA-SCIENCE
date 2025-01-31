"""
PROBLEM 3
Write a program to display only those numbers from a list that satisfy the following conditions
● The number must be divisible by five
● If the number is greater than 150, then skip it and move to the next number
● If the number is greater than 500, then stop the loop
"""

def filter_num(numbers):
    res = []
    for num in numbers:
        if num > 500:
            break
        if num > 150:
            continue
        if num % 5 == 0:
            res.append(num)
    return res

num_l1 = [12, 75, 150, 180, 145, 525, 50]
print("Output:", filter_num(num_l1))

num_l2 = [14, 85, 625, 75]
print("Output:", filter_num(num_l2))