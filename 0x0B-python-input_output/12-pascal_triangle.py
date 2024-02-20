#!/usr/bin/python3
"""Create a function"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    if n <= 0:
        return []
    tr = [[1]]
    while len(tr) != n:
        trt = [1]
        trn = tr[-1]

        for t in range(len(trn) - 1):
            trt.append(trn[t] + trn[t + 1])

        trt.append(1)
        tr.append(trt)

    return tr
