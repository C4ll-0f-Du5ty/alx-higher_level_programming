#!/usr/bin/python3
""" Starting with files"""


def read_file(filename=""):
    """Reading from a given file"""
    with open(filename, encoding='UTF-8') as file:
        print(file.read(), end="")
