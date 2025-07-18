"""
Problem 3: Given an array of N integers and a number K, the task is to find the number of pairs of integers in the array whose sum is equal to K.

Test Case 1:

Input: arr[] = {1, 5, 7, -1}, sum = 6

Output: 2

Explanation: Pairs with sum 6 are (1, 5) and (7, -1).

Test Case 2:

Input: arr[] = {1, 5, 7, -1, 5}, sum = 6

Output: 3

Explanation: Pairs with sum 6 are (1, 5), (7, -1) & (1, 5)
"""

def count_pairs_with_sum(arr, K):
    freq_map = {}
    count = 0

    for num in arr:
        complement = K - num
        if complement in freq_map:
            count += freq_map[complement]
        freq_map[num] = freq_map.get(num, 0) + 1

    return count

arr1 = [1, 5, 7, -1]
K1 = 6
print(count_pairs_with_sum(arr1, K1))

arr2 = [1, 5, 7, -1, 5]
K2 = 6
print(count_pairs_with_sum(arr2, K2))