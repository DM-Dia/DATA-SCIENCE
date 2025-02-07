"""

Problem 1: Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i!= j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Test Cases: 1

Input: nums = [-1,0,1,2,-1,-4]

Output :
[-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

Test Case 2:

Input: nums = [0,1,1]

Output: []

Explanation: The only possible triplet does not sum up to 0.

Test Case 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]

Explanation: The only possible triplet sums up to 0.
"""

def three_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):  # Iterate through the array
        if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1  # Increase sum
            else:
                right -= 1  # Decrease sum

    return result

# Test cases
print(three_sum([-1, 0, 1, 2, -1, -4]))
print(three_sum([0, 1, 1]))
print(three_sum([0, 0, 0]))