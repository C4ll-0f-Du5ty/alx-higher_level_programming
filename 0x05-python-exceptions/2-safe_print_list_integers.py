#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    g = 0
    while g < x:
        try:
            print("{:d}".format(my_list[g]), end="")
            counter += 1
        except (ValueError, TypeError):
            pass
        g += 1
    print()
    return counter
