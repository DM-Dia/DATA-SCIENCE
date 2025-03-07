#1. Write a Python program to create a tuple with different data types.

my_tup = (10, "ABCdef", 5.61, True, [1, 4, 3])
print("Tuple with different data types:", my_tup)

#2. Write a Python program to create a tuple of numbers and print one item.

numt = (5, 10, 15, 20, 25)
print("One item from tuple:", numt[1])

#3. Write a Python program to add an item to a tuple.

original_tuple = (1, 2, 3)
new_tuple = original_tuple + (5,)
print("Tuple after adding an item:", new_tuple)

#4. Write a Python program to get the 4th element from the last element of a Tuple.

stuple = (10, 20, 30, 40, 50, 60, 70, 80)
fourth_from_last = stuple[-4]
print("4th element from the last:", fourth_from_last)

#5. Write a Python program to convert a tuple to a dictionary.

tuple_data = (("name", "abc"), ("age", 25), ("city", "xyz"))
dictionary = dict(tuple_data)
print("Converted dictionary:", dictionary)

'''6. Write a Python program to replace the last value of tuples in a list.
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]'''

sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
updated_list = [t[:-1] + (100,) for t in sample_list]
print("Updated list:", updated_list)