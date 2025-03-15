class SparseVector:
    def __init__(self, nums):
        # Store non-zero values with their indices
        self.data = {i: num for i, num in enumerate(nums) if num != 0}

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        # Iterate through the smaller dictionary for efficiency
        if len(self.data) < len(vec.data):
            for i, val in self.data.items():
                if i in vec.data:
                    result += val * vec.data[i]
        else:
            for i, val in vec.data.items():
                if i in self.data:
                    result += val * self.data[i]
        return result

# Example Usage
nums1 = [1,0,0,2,3]
nums2 = [0,3,0,4,0]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
print(v1.dotProduct(v2))  # Output: 8

nums1 = [0,1,0,0,0]
nums2 = [0,0,0,0,2]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
print(v1.dotProduct(v2))  # Output: 0

nums1 = [0,1,0,0,2,0,0]
nums2 = [1,0,0,0,3,0,4]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
print(v1.dotProduct(v2))  # Output: 6