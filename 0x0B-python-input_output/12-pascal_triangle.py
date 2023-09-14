#!/usr/bin/python3
"""returns a list of lists of integers representing
the Pascal’s triangle of n"""


def pascal_triangle(n):
    """function
    arg:
        n: int
    """
    lout = []
    if n > 0:
        for i in range(n):
            lin = []
            for j in range(i + 1):
                if not j:
                    lin.append(1)
                elif j == i:
                    lin.append(1)
                else:
                    lin.append(lout[i - 1][j - 1] + lout[i - 1][j])
            lout.append(lin)
    return lout
