#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 1000}
    result = 0
    rev_roman = reversed(roman_string)
    for i in rev_roman:
        if result > 3999 or result < 0:
            break
        if result < roman_numbers[i] * 4:
            result += roman_numbers[i]
        else:
            result -= roman_numbers[i]
    return result
