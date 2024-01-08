#!/usr/bin/python3
"""sorting list module and printing
    it
"""


class MyList(list):
    """Function to return a sorted list
    and then printing it
    """
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
