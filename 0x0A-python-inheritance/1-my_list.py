#!/usr/bin/python3
"""sorting list module and printing 
    it
"""


class MyList(list):
    """Function to return a sorted list
    and then printing it
    """
    def __init__(self):
        super().__init__()

    for l in list:
        if not isinstance(l, int):
            raise TypeError
    def print_sorted(self):
        print(sorted(self))
