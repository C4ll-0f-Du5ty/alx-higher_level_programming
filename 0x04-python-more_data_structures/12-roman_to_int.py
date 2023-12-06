#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or isinstance(roman_string, str) is False:
        return 0
    num = 0
    for i in roman_string:
        if i == 'X':
            if 0 < num < 10:
                num = 10 - num
            else:
                num += 10
        elif i == 'I':
            num += 1
        elif i == 'V':
            if 0 < num < 5:
                num = 5 - num
            else:
                num += 5
        elif i == 'L':
            if 0 < num < 50:
                num = 50 - num
            else:
                num += 50
        elif i == 'C':
            if 0 < num < 100:
                num = 100 - num
            else:
                num += 100
        elif i == 'D':
            if 0 < num < 500:
                num = 500 - num
            else:
                num += 500
        elif i == 'M':
            if 0 < num < 1000:
                num = 1000 - num
            else:
                num += 1000
    return num
