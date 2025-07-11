"""
PROBLEM 7

Write a program to Use a loop to display elements from a given list present at odd index position

Test Case 1:

Input: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100

Output: [20, 40, 60, 80, 100]

Test Case 2:

Input: 23, 46, 69, 92, 115

Output: [46, 92]
"""

def elem_odd_indices(inl):
    res = []
    for i in range(1, len(inl), 2):  # Start from index 1 and increment by 2
        res.append(inl[i])
    return res

# Test Case 1
inl1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Output:", elem_odd_indices(inl1))

# Test Case 2
inl2 = [23, 46, 69, 92, 115]
print("Output:", elem_odd_indices(inl2))