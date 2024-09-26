#!/usr/bin/python3
"""
tihs module will returns the perimeter of the island described in grid.
"""


def island_perimeter(grid):
    """
    function def island_perimeter(grid):
    that returns the perimeter of the island described
    """

    gd = 0
    for ld in range(len(grid)):
        for gd in range(len(grid[ld])):
            if (grid[ld][gd] == 1):
                if (ld <= 0 or grid[ld - 1][gd] == 0):
                    gd += 1
                if (ld >= len(grid) - 1 or grid[ld + 1][gd] == 0):
                    gd += 1
                if (gd <= 0 or grid[ld][gd - 1] == 0):
                    gd += 1
                if (gd >= len(grid[ld]) - 1 or grid[ld][gd + 1] == 0):
                    gd += 1
    return gd
