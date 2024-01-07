#!/usr/bin/python3
"""Module to print a given size in square
"""


def print_square(size):
    """Function to print a square depending on a
    number passed to the function
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ZeroDivisionError("size must be >= 0")

    for _ in range(size):
        print('#' * size)
