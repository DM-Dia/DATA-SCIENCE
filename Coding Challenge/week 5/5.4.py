from typing import List

def singleNum(nums: List[int]) -> List[int]:
    # Step 1: XOR all numbers to get XOR of two unique numbers (a ⊕ b)
    xor_all = 0
    for num in nums:
        xor_all ^= num

    # Step 2: Find rightmost set bit in xor_all
    rightmost_bit = xor_all & -xor_all

    # Step 3: Partition numbers into two groups and XOR within each group
    num1, num2 = 0, 0
    for num in nums:
        if num & rightmost_bit:
            num1 ^= num
        else:
            num2 ^= num
    return [num1, num2]

# Test Cases
print(singleNum([1,2,1,3,2,5]))
print(singleNum([-1,0]))
print(singleNum([0,1]))