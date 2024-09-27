#!/usr/bin/python3
""" A module that defines a island_perimeter function """


def island_perimeter(grid):
    """It returns the perimeter of the island described in grid"""
    perimeter = 0
    n = len(grid)
    m = len(grid[0]) if n > 0 else 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
