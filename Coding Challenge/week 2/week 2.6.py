def roman_to_int(s):
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev_value = 0
    for char in reversed(s):
        curr_value = roman_map[char]
        if curr_value < prev_value:
            total -= curr_value
        else:
            total += curr_value
        prev_value = curr_value

    return total
print(roman_to_int("III"))
print(roman_to_int("LVIII"))
print(roman_to_int("MCMXCIV"))