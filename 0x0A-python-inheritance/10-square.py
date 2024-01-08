#!/usr/bin/python3
"""inheritance example module
"""


module = __import__('9-rectangle')
rectangle = getattr(module, 'Rectangle')


class Square(rectangle):
    """new class to set some
    attributes
"""
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}"
