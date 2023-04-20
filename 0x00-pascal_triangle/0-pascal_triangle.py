#!/usr/bin/python3
"""
A function that Implements a Representation of Pascal's Triangle
"""

def pascal_triangle(n):
    if n <= 0:
        return []

    # Initialize the first row
    triangle = [[1]]

    # Compute the subsequent rows of the triangle
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
