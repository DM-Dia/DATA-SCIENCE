def remDupl(s: str) -> str:
    stack = []
    for char in s:
        if stack and stack[-1] == char:  # Check if top element matches cur char
            stack.pop()  # Remove duplicate
        else:
            stack.append(char)  # Push non-duplicate character
    return ''.join(stack)  # Convert stack back to a string

#Test Cases
print(remDupl("abbaca"))  # Output: "ca"
print(remDupl("azxxzy"))  # Output: "ay"