#!/usr/bin/python3
""" adds 2 integers!
        a(int) required first index
        b(int) optional second index
        raise: an error when the passed value not integer
    """


def add_integer(a, b=98):
    """ adds 2 integers
        and raises an error in type or value
    """
    try:
        x = int(a)
    except (ValueError, TypeError):
        raise TypeError("a must be an integer")
    else:
        try:
            y = int(b)
        except (ValueError, TypeError):
            raise TypeError("b must be an integer")

    return x + y
