#!/usr/bin/python3
"""checking the type of an
    object
"""


def inherits_from(obj, a_class):
    """return true or false depending
        on the provided object if it an
        instnace of the provided class
    """
    return isinstance(obj, a_class) and type(obj) != a_class
