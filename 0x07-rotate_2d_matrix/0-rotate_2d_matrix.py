#!/usr/bin/python3
"""A module that defines a function  for rotating a 2D matrix"""


def rotate_2d_matrix(matrix):
    """It rotates a 2D matrix by 90 degrees clockwise"""
    if not isinstance(matrix, list):
        return
    if len(matrix) < 1 or not all(isinstance(r, list) for r in matrix):
        return

    row = len(matrix)
    col = len(matrix[0])
    if not all(len(row) == col for row in matrix):
        return

    rotated_matrix = []
    for col in range(col):
        rotated_matrix.append(
            [matrix[row][col] for row in range(row-1, -1, -1)])
    for row in range(row):
        matrix[row] = rotated_matrix[row]
