#!/usr/bin/python3
"""appending a string a string """


def append_write(filename="", text=""):
    """appending a string a string """
    with open(filename, 'a', encoding='UTF-8') as f:
        return f.write(text)
