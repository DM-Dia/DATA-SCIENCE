def maxCrossingSum(nums, left, mid, right):
    # Compute max sum of left subarray ending at mid
    left_sum = float('-inf')
    temp_sum = 0
    for i in range(mid, left-1, -1):
        temp_sum += nums[i]
        left_sum = max(left_sum, temp_sum)

    # Compute max sum of right subarray starting from mid+1
    right_sum = float('-inf')
    temp_sum = 0
    for i in range(mid+1, right+1):
        temp_sum += nums[i]
        right_sum = max(right_sum, temp_sum)
    return left_sum + right_sum

def maxSubArray(nums, left, right):
    if left == right:
        return nums[left]
    mid = (left + right) // 2
    left_max = maxSubArray(nums, left, mid)  # Max sum in left half
    right_max = maxSubArray(nums, mid+1, right)  # Max sum in right half
    cross_max = maxCrossingSum(nums, left, mid, right)  # Max sum across middle
    return max(left_max, right_max, cross_max)

def maxSubArray_dc(nums):
    return maxSubArray(nums, 0, len(nums) - 1)

# Test Cases
print(maxSubArray_dc([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
print(maxSubArray_dc([1]))                      # Output: 1
print(maxSubArray_dc([5,4,-1,7,8]))             # Output: 23