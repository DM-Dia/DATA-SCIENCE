import numpy as np

# Create a 1D Numpy array “a” containing 10 random integers between 0 and 99
a = np.random.randint(0, 100, 10)
print("1D Array a:", a)

# Create a 2D Numpy array “b” of shape (3, 4) containing random integers between -10 and 10
b = np.random.randint(-10, 11, (3, 4))
print("2D Array b:\n", b)

# Reshape “b” into a 1D Numpy array “b_flat”
b_flat = b.flatten()
print("Flattened Array b_flat:", b_flat)

# Create a copy of “a” called “a_copy”, and set the first element of “a_copy” to -1
a_copy = a.copy()
a_copy[0] = -1
print("Original a:", a)
print("Modified a_copy:", a_copy)

# Create a 1D Numpy array “c” containing every second element of “a”
c = a[::2]
print("Array c (every second element of a):", c)

"""**2: Numpy array indexing and slicing**"""

# Print the third element of “a”
print("Third element of a:", a[2])

# Print the last element of “b”
print("Last element of b:", b[-1, -1])

# Print the first two rows and last two columns of “b”
print("First two rows and last two columns of b:\n", b[:2, -2:])

# Assign the second row of “b” to a variable called “b_row”
b_row = b[1, :]
print("Second row of b:", b_row)

# Assign the first column of “b” to a variable called “b_col”
b_col = b[:, 0]
print("First column of b:", b_col)

"""**3: Numpy array operations**"""

# Create a 1D Numpy array “d” containing the integers from 1 to 10
d = np.arange(1, 11)
print("Array d:", d)

# Add “a” and “d” element-wise to create a new Numpy array “e”
e = a + d
print("Element-wise addition of a and d:", e)

# Multiply “b” by 2 to create a new Numpy array “b_double”
b_double = b * 2
print("b multiplied by 2:\n", b_double)

# Calculate the dot product of “b” and “b_double” to create a new Numpy array “f”
f = np.dot(b, b_double.T)
print("Dot product of b and b_double:\n", f)

# Calculate the mean of “a”, “b”, and “b_double” to create a new Numpy array “g”
g = np.array([np.mean(a), np.mean(b), np.mean(b_double)])
print("Mean values of a, b, and b_double:", g)

"""**4: Numpy array aggregation**"""

# Find the sum of every element in “a” and assign it to a variable “a_sum”
a_sum = np.sum(a)
print("Sum of all elements in a:", a_sum)

# Find the minimum element in “b” and assign it to a variable “b_min”
b_min = np.min(b)
print("Minimum element in b:", b_min)

# Find the maximum element in “b_double” and assign it to a variable “b_double_max”
b_double_max = np.max(b_double)
print("Maximum element in b_double:", b_double_max)