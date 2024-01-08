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
        self.integer_validator(width, height)
        self.__width = width
        self.__height = height

