#!/usr/bin/python3
"""inheritance example module
"""


module = __import__('9-rectangle')
Rectangle = getattr(module, 'Rectangle')


class Square(Rectangle):
    """new class to set some
    attributes
"""
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2
