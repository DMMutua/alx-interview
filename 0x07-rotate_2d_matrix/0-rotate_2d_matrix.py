#!/usr/bin/python 3
"""A Script with a function for 2D Matrix Rotation"""


def rotate_2d_matrix(matrix):
    """ A Function that Rotates a 2D Matrix 90 Degrees In-Place.
    Assumes that the Matrix will Not Be Empty and is 2D
    """
    l, r = 0, len(matrix) - 1

    while l < r:
        for i in range(r - l):
            top, bottom = l, r

            # Saving topleft
            topLeft = matrix[top][l + i]

            # Move bottom left into top left; shifting up
            matrix[top][l + i] = matrix[bottom - i][l]

            # Move bottom right into bottom left; shifting across
            matrix[bottom - i][l] = matrix[bottom][r - i]

            # Move Top Right into bottom right
            matrix[bottom][r - i] = matrix[top + i][r]

            # Move top left into top right
            matrix[top + i][r] = topLeft

        # Move into Inner Submatrices if available..
        r -= 1
        l += 1

