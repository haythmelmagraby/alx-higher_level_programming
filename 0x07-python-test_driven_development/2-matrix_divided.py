#!/usr/bin/python3
""" Divide a matrix"""


def matrix_divided(matrix, div):

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix" +
                " (list of lists) of integers/floats")
    if not isinstance(div, (float,int)):
        raise TypeError("div must be a number")

    for n in matrix:
        if not isinstance(n, list) or len(n) == 0:
            raise TypeError("matrix must be a matrix" +
                " (list of lists) of integers/floats")
        if len(matrix) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have"+
                    " the same size")
        for i in n:
            if not isinstance(i, list) or len(i) == 0:
                raise TypeError("matrix must be a matrix" +
                        " (list of lists) of integers/floats")
        return [[round(i / div, 2) for i in n] for n in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
