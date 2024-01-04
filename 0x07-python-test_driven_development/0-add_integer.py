#!/usr/bin/python3
def add_integer(a, b=98):
    try:
        x = int(a)
    except (ValueError, TypeError):
        raise TypeError("a must be an integer")
    else:
        try:
            y = int(b)
        except (ValueError, TypeError):
            raise TypeError("b must be an integer")
        
    return x + y
