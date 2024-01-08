#!/usr/bin/python3
"""checking the type
"""


def is_same_class(obj, a_class):
    """return true or false depending
    on the provided object if it an
    instnace of the provided class
"""
    if isinstance(obj, a_class):
        return True
    return False
