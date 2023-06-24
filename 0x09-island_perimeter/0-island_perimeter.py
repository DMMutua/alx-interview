#!/usr/bin/python3
""" Module with function to solve Island Problem"""


def island_perimeter(grid):
    """A Function that returns the Island Perimiter
    In a Grid of Square Blocks of Land where 1 Reps
    Land and 2 Reps Water
    """
    if len(grid) >= 100 or len(grid[0]) > 100:
        raise ValueError

    visited = set()

    def dfs(i, j):
        """A depth first search Algorithm"""

        if i >= len(grid) or j >= len(grid[0]) \
                or i < 0 or j < 0 or grid[i][j] == 0:
            return 1
        if (i, j) in visited:
            return 0

        # Add Visited cells to set
        visited.add((i, j))
        # Go to All directions in Grid using dfs
        perimeter = dfs(i, j + 1)
        perimeter += dfs(i + 1, j)
        perimeter += dfs(i, j - 1)
        perimeter += dfs(i - 1, j)
        return perimeter

    # Iterate over grid to find atleast one land cell to start search
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                return dfs(i, j)
