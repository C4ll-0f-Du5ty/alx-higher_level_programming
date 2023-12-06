#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    num = 0
    for i in roman_string:
        if i == 'X':
            num += 10
        elif i == 'I':
            num += 1
        elif i == 'V':
            num += 5
        elif i == 'L':
            num += 50
        elif i == 'C':
            num += 100
        elif i == 'D':
            num += 500
        elif i == 'M':
            num += 1000
    return num
