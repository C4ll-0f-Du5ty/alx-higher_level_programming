#!/usr/bin/python3
"""inheritance example module
"""


module = __import__('7-base_geometry')
BaseGeometry = getattr(module, 'BaseGeometry')


class Rectangle(BaseGeometry):
    """new class to set some
    attributes
"""
    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
