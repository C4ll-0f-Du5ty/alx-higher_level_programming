#!/usr/bin/python3
"""Module to print a full name
"""


def say_my_name(first_name, last_name=""):
    """Function to print a full name of a
    person by passing his first and last names
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
