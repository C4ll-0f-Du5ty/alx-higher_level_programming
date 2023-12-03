#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    g = my_list[:]
    if idx < 0 or idx > len(g) - 1:
        return g
    else:
        g[idx] = element
        return (g)
