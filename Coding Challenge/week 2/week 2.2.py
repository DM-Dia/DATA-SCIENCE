"""
Problem 2: Given an array of positive and negative numbers, arrange them such that all negative integers appear before all the positive integers in the array without using any additional data structure like a hash table, arrays, etc. The order of appearance should be maintained.

Test case 1:

Input: -12, 11, -13, -5, 6, -7, 5, -3, -6

Output: -12 -13 -5 -7 -3 -6 11 6 5

Test case 2:

Input: -12, 11, 13, -5, 6, -7, 5, -3, 8

Output: -12 -5 -7 -3 11 13 6 5 8
"""

def rearr_array(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]

        # If the current element is negative, we need to shift
        if key < 0:
            j = i - 1
            while j >= 0 and arr[j] >= 0:
                arr[j + 1] = arr[j]  # Shift positive elements right
                j -= 1

            arr[j + 1] = key  # Place negative element at correct position

    return arr


arr1 = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
arr2 = [-12, 11, 13, -5, 6, -7, 5, -3, 8]

print(rearr_array(arr1))
print(rearr_array(arr2))