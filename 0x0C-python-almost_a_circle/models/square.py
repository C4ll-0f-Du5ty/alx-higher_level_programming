#!/usr/bin/python3
"""Square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """a new Class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """The message for printing the instance of the class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
