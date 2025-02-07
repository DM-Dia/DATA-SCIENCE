def int_to_roman(num):
    roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    result = []

    for value, symbol in roman_map:
        while num >= value:
            result.append(symbol)
            num -= value

    return ''.join(result)

print(int_to_roman(3749))  # Output: "MMMDCCXLIX"
print(int_to_roman(58))    # Output: "LVIII"
print(int_to_roman(1994))  # Output: "MCMXCIV"