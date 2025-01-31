"""
PROBLEM 2
You have been given a string. You need to remove all the duplicates from the string. The nal output string should contain each character only once. 
The respective order of the characters inside the string should remain the same. You can traverse the string only once.
"""

def rem_dup(string):
    s = set()
    res = []
    for char in string:
        if char not in s:
            s.add(char)
            res.append(char)
    return ''.join(res)

#in_str = "abaabbbacd"
in_str = input("Enter: ")
out_str = rem_dup(in_str)
print("Input String:", in_str)
print("Output String:", out_str)