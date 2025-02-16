def max_triplet_sort(arr):
    arr.sort()  # Sort the array
    n = len(arr)

    # Two possible triplets for maximum product
    product1 = arr[n-1] * arr[n-2] * arr[n-3]  # Three largest elements
    product2 = arr[0] * arr[1] * arr[n-1]      # Two smallest and largest element

    if product1 > product2:
        return (arr[n-3], arr[n-2], arr[n-1])
    else:
        return (arr[0], arr[1], arr[n-1])

#test cases
print("The triplet having the maximum product is", max_triplet_sort([-4, 1, -8, 9, 6]))  # Output: (-8, -4, 9)
print("The triplet having the maximum product is", max_triplet_sort([1, 7, 2, -2, 5]))  # Output: (7, 5, 2)