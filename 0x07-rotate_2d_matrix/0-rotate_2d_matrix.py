#!/usr/bin/python 3
"""A Script with a function for 2D Matrix Rotation"""

from typing import List


def rotate_2d_matrix(matrix: List[List[int]]) -> None:
    """ A Function that Rotates a 2D Matrix 90 Degrees In-Place.
    Assumes that the Matrix will Not Be Empty and is 2D
    """
    n: int = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
