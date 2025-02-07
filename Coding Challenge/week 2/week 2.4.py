"""
Problem 4: Given an array of N integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that:

a. Each student gets one packet.

b. The difference between the number of chocolates in the packet with maximum
chocolates and the packet with minimum chocolates given to the students is
Minimum.

Test Case 1

Input: arr[] = {7, 3, 2, 4, 9, 12, 56}, m = 3

Output: Minimum Difference is 2

Explanation:
We have seven packets of chocolates and we need to pick three packets for 3 students. If we pick 2, 3, and 4, we get the minimum difference between maximum and minimum packet sizes.

Test Case 2

Input: arr[] = {3, 4, 1, 9, 56, 7, 9, 12}, m = 5

Output: Minimum Difference is 6
"""

def min_choco_diff(arr, m):
    if m == 0 or len(arr) == 0:
        return 0
    n = len(arr)
    if n < m:
        return -1
    arr.sort()
    min_diff = float('inf')
    for i in range(n - m + 1):
        diff = arr[i + m - 1] - arr[i]
        min_diff = min(min_diff, diff)
    return min_diff
arr1 = [7, 3, 2, 4, 9, 12, 56]
m1 = 3
print("Minimum Difference is", min_choco_diff(arr1, m1))

arr2 = [3, 4, 1, 9, 56, 7, 9, 12]
m2 = 5
print("Minimum Difference is", min_choco_diff(arr2, m2))