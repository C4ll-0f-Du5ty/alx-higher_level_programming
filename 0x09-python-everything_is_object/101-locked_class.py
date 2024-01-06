#!/usr/bin/python3
"""This is a module that demonstrates the use of __slots__."""


class LockedClass:
    """
    Attributes:
    - allowed_attribute: An attribute that users can assign values to.
    'Hello'
    """

    __slots__ = ['first_name']
