#!/usr/bin/python3
"""sorting list module
    """

class MyList(list):
    """Function to return a sorted list
    """
    def __init__(self):
        super().__init__()
    
    def print_sorted(self):
        print(sorted(self))
