#!/usr/bin/python3
"""A moduel that return the pascal triangle"""


def pascal_triangle(n):
    """
    It return n rows of Pascal's triangle as a list of lists of integers.
    """
    if n <= 0:
        return []
    tri = []
    for x in range(n):
        r = [1]
        for j in range(1, x):
            r.append(tri[x - 1][j - 1] + tri[x - 1][j])
        if x > 0:
            r.append(1)
        tri.append(r)
    return tri
