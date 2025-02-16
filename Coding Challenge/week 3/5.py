def permutation(num):
    n = len(num)
    i = n - 2  # Start from second last element

    # Step 1: Find the first decreasing element from the right
    while i >= 0 and num[i] >= num[i + 1]:
        i -= 1

    if i >= 0:  # Step 2: Find the next greater element to swap
        j = n - 1
        while num[j] <= num[i]:
            j -= 1
        num[i], num[j] = num[j], num[i]  # Swap

    # Step 3: Reverse the elements to the right of i
    num[i + 1:] = reversed(num[i + 1:])

# Test Cases
arr1 = [1, 2, 3]
permutation(arr1)
print(arr1)  # Output: [1, 3, 2]

arr2 = [3, 2, 1]
permutation(arr2)
print(arr2)  # Output: [1, 2, 3]

arr3 = [1, 1, 5]
permutation(arr3)
print(arr3)  # Output: [1, 5, 1]