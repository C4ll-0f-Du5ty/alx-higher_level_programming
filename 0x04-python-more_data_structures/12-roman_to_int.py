#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    romanD = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0
    lastOne = 0
    for char in reversed(roman_string):
        value = romanD.get(char, 0)
        if lastOne <= value:
            sum += value
        else:
            sum -= value
        lastOne = value
    return sum
