#!/usr/bin/python3
"""checking the type
"""


def is_same_class(obj, a_class):
    """return true or false depending
    on the provided object if it an
    instnace of the provided class
"""
    return type(obj) is a_class
