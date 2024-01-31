#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_number = {
        "M": 1000, "D": 500, "C": 100, "X": 10, "L": 50, "V": 5, "I": 1
        }
    if roman_string is None or type(roman_string) is not str:
        return 0
    num = 0
    prev = 0

    for i in roman_string:
        val = roman_number[i]
        if val > prev:
            num = num + val - 2 * prev
        else:
            num = num + val
        prev = val
    return num
