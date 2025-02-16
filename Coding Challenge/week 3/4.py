def trap_rain_water(arr):
    if not arr or len(arr) < 3:
        return 0  # Water can't be trapped with less than 3 bars

    left, right = 0, len(arr) - 1
    left_max, right_max = 0, 0
    water = 0

    while left < right:
        if arr[left] < arr[right]:  # Process the smaller side
            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                water += left_max - arr[left]
            left += 1  # Move left pointer
        else:
            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                water += right_max - arr[right]
            right -= 1  # Move right pointer

    return water

# Test Cases
print(trap_rain_water([0, 2, 0, 2, 0]))  # Output: 2
print(trap_rain_water([0,1,0,2,1,0,1,3,2,1,2,1,0]))  # Output: 6