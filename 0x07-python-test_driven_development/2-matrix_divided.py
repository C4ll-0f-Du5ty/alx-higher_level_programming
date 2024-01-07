#!/usr/bin/python3
""" dividing matrix
        matrix (list of list)
        div (number to divide by)
        raise: errors when encountered
    """


def matrix_divided(matrix, div):
    """ we make sure of the data types
        and putting our exceptions
    """
    for row in matrix:
        for col in row:
            try:
                num = int(col)
            except ValueError:
                raise ValueError("matrix must be a matrix (list of lists) "
                                 "of integers/floats")

    Row = len(matrix[0])
    if not all(Row == len(row) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if num == 0:
        raise ZeroDivisionError("division by zero")

    new = [[round(col / div, 2) for col in row] for row in matrix]

    return new
