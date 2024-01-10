#!/usr/bin/python
"""couting the characters of a string """


def write_file(filename="", text=""):
    """returning the number of characters """
    with open(filename, 'w', encoding='UTF-8') as f:
        return f.write(text)
