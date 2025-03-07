#1 Write a Python script to sort (ascending and descending) a dictionary by value.
my_dict = {'a': 40, 'b': 10, 'c': 25, 'd': 30}
sorted_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending order:", sorted_asc)
sorted_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending order:", sorted_desc)

#2. Write a Python program to iterate over dictionaries using for loops.
person = {'name': 'A', 'age': 25, 'city': 'xyz'}
for key, value in person.items():
    print(f"{key}: {value}")

#3. Write a Python script to merge two Python dictionaries.
dict1 = {'a': 10, 'b': 20}
dict2 = {'c': 30, 'd': 40}
merged_dict = dict1.copy()
merged_dict.update(dict2)
print("Merged dictionary:", merged_dict)

#4. Write a Python program to sum all the items in a dictionary.
num_dict = {'a': 10, 'b': 20, 'c': 30}
total_sum = sum(num_dict.values())
print("Sum of all values:", total_sum)

#5. Write a Python program to multiply all the items in a dictionary.
from functools import reduce
num_dict = {'a': 2, 'b': 3, 'c': 4}
product = reduce(lambda x, y: x * y, num_dict.values())
print("Product of all values:", product)

#6.Write a Python program to sort a given dictionary by key.
my_dict = {'b': 10, 'a': 40, 'c': 25, 'd': 30}
sorted_dict = dict(sorted(my_dict.items()))
print("Dictionary sorted by key:", sorted_dict)

#7. Write a Python program to remove duplicates from the dictionary
sample_dict = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 20}
unique_dict = {}
for key, value in sample_dict.items():
    if value not in unique_dict.values():
        unique_dict[key] = value
print("Dictionary after removing duplicates:", unique_dict)