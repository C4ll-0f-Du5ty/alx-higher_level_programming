#!/usr/bin/python
"""couting the characters of a string """


def write_file(filename="", text=""):
    """returning the number of characters """
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write(text)
    return len(text) - 1
