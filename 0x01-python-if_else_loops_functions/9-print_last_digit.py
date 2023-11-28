#!/usr/bin/python3
def print_last_digit(number):
    s = abs(number) % 10
    print(s, end="")
    return s
