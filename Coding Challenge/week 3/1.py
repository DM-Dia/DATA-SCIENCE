def longest_subarray_with_sum_k(arr, k):
    pre_sum = 0
    sum_map = {}
    max_length = 0

    for i, num in enumerate(arr):
        pre_sum += num  # Update prefix sum

        # Check if the whole subarray from index 0 to i has sum = k
        if pre_sum == k:
            max_length = i + 1  # Full subarray has sum k

        # Check if (prefix_sum - k) exists in the map
        if (pre_sum - k) in sum_map:
            max_length = max(max_length, i - sum_map[pre_sum - k])

        # Store prefix_sum if it's not already present
        if pre_sum not in sum_map:
            sum_map[pre_sum] = i  # Store only the first occurrence

    return max_length

#test cases
print(longest_subarray_with_sum_k([10, 5, 2, 7, 1, -10], 15))  # Output: 6
print(longest_subarray_with_sum_k([-5, 8, -14, 2, 4, 12], -5))  # Output: 5
print(longest_subarray_with_sum_k([10, -10, 20, 30], 5))  # Output: 0