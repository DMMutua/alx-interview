#!/usr/bin/python3
"""A Script with a function for 2D Matrix Rotation"""


def rotate_2d_matrix(matrix):
    """ A Function that Rotates a 2D Matrix 90 Degrees In-Place.
    Assumes that the Matrix will Not Be Empty and is 2D
    """
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right

            # Saving topleft
            topLeft = matrix[top][left + i]

            # Move bottom left into top left; shifting up
            matrix[top][left + i] = matrix[bottom - i][left]

            # Move bottom right into bottom left; shifting across
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # Move Top Right into bottom right
            matrix[bottom][right - i] = matrix[top + i][right]

            # Move top left into top right
            matrix[top + i][right] = topLeft

        # Move into Inner Submatrices if available..
        right -= 1
        left += 1
