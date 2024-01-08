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
        for item in self:
           if not isinstance(item, int):
               raise TypeError("All items in the list must be integers.")

    
    def print_sorted(self):
        print(sorted(self))
