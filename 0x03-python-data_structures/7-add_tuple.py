#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    a3 = tuple_b[0] if len(tuple_b) > 0 else 0
    a4 = tuple_b[1] if len(tuple_b) > 1 else 0

    return (a1 + a3, a2 + a4)
