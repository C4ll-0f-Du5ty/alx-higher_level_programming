#!/usr/bin/python3
"""Module to make indentation of a string
"""


def text_indentation(text):
    """Function to modify a string depending on
    a given delimeters and display the changes
    """
    flag = False
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    deli = ['.', '?', ':']
    for char in text:
        if flag:
            flag = False
            if char == " ":
                continue
        if char == '.' or char == '?' or char == ':':
            print(char, end="")
            print("\n")
            flag = True
            continue
        print(char, end="")
