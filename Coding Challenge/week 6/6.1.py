def productExceptSelf(num):
    n = len(num)
    ans = [1] * n  # Initialize the result array

    # Compute prefix products
    prefix = 1
    for i in range(n):
        ans[i] = prefix
        prefix *= num[i]

    # Compute suffix products
    suffix = 1
    for i in range(n-1, -1, -1):
        ans[i] *= suffix
        suffix *= num[i]

    return ans

#test cases
print(productExceptSelf([1,2,3,4]))  # Output: [24,12,8,6]
print(productExceptSelf([-1,1,0,-3,3]))  # Output: [0,0,9,0,0]