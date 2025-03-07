from functools import reduce
#Write a Python program to multiply all the items in a list.
def multiply_list(lst):
    return reduce(lambda x, y: x * y, lst, 1)
print(multiply_list([1, 2, 3, 4]))  # Output: 24

#Write a Python program to get the largest number from a list.
def max_in_list(lst):
    return max(lst)
print(max_in_list([10, 20, 5, 8]))  # Output: 20

#Write a Python program to get the smallest number from a list.
def min_in_list(lst):
    return min(lst)
print(min_in_list([10, 20, 5, 8]))  # Output: 5

'''Write a Python program to get a list, sorted in increasing order by the last
element in each tuple from a given list of non-empty tuples.'''
def sort_by_last_element(tuples):
    return sorted(tuples, key=lambda x: x[-1])
print(sort_by_last_element([(1, 3), (4, 2), (2, 5)]))  # Output: [(4, 2), (1, 3), (2, 5)]

'''Write a Python program to remove duplicates from a list.'''
def remove_duplicates(lst):
    return list(set(lst))
print(remove_duplicates([1, 2, 2, 3, 4, 4]))  # Output: [1, 2, 3, 4]

'''Write a Python program to check if a list is empty or not.'''
def is_list_empty(lst):
    return len(lst) == 0
print(is_list_empty([]))  # Output: True

'''Write a Python program to count the lowercase letters in a given list of Word'''
def count_lowercase(lst):
    return sum(sum(1 for ch in word if ch.islower()) for word in lst)
print(count_lowercase(['Hello', 'World', 'Python']))  # Output: 10

''''Write a Python program to extract specified number of elements from a
given list, which follows each other continuously.
○ Original list: [1, 1, 3, 4, 4, 5, 6, 7]
○ Extract 2 number of elements from the said list which follows each
other continuously: [1, 4]
○ Original list: [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
○ Extract 4 number of elements from the said list which follows each
other continuously: [4]'''
def extract_continuous_elements(lst, n):
    return [x for x in set(lst) if lst.count(x) >= n]
print(extract_continuous_elements([1, 1, 3, 4, 4, 5, 6, 7], 2))  # Output: [1, 4]

'''Write a Python program to find the largest odd number in a given list of
integers.
○ Sample Data: ([0, 9, 2, 4, 5, 6]) -> 9
 ([-4, 0, 6, 1, 0, 2]) -> 1
 ([1, 2, 3]) -> 3
 ([-4, 0, 5, 1, 0, 1]) -> 5 '''
def largest_odd(lst):
    odds = [x for x in lst if x % 2 == 1]
    return max(odds) if odds else None
print(largest_odd([0, 9, 2, 4, 5, 6]))  # Output: 9

'''Write a Python program to print a specified list after removing the 0th, 4th
and 5th elements.
○ Sample List : [A, B, C, D, E, F]
○ Expected Output : [B, C, D]'''
def remove_specific_indices(lst):
    return [lst[i] for i in range(len(lst)) if i not in [0, 4, 5]]
print(remove_specific_indices(['A', 'B', 'C', 'D', 'E', 'F']))