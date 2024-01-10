#!/usr/bin/python
"""couting the characters of a string """


def write_file(filename="", text=""):
    """returning the number of characters """
    count = 0
    with open(filename, encoding='UTF-8') as f:
        for s in text:
            f.write(s)
            count += 1
    return count
