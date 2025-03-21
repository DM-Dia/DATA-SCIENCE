def countConsistentStrings(allowed: str, words: list) -> int:
    allowed_set = set(allowed)  # Convert allowed characters to a set for O(1) lookup
    count = 0

    for word in words:
        if all(char in allowed_set for char in word):  # Check if all chars in allowed
            count += 1

    return count

print(countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))  # Output: 2
print(countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"]))  # Output: 7
print(countConsistentStrings("cad", ["cc","acd","b","ba","bac","bad","ac","d"]))  # Output: 4