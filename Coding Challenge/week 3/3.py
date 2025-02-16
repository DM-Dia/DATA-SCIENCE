def three_sum(nums):
    nums.sort()  # Step 1: Sort the array
    n = len(nums)
    res = []

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:  # Avoid duplicate triplets
            continue

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                res.append([nums[i], nums[left], nums[right]])

                # Move pointers and avoid duplicates
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1  # Increase sum by moving left pointer
            else:
                right -= 1  # Decrease sum by moving right pointer

    return res

#test cases
print(three_sum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1,-1,2],[-1,0,1]]
print(three_sum([0, 1, 1]))              # Output: []
print(three_sum([0, 0, 0]))              # Output: [[0, 0, 0]]