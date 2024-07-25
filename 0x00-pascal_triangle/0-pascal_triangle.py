#!/usr/bin/python3
""" This Module for Pascal's Triangle
"""


def pascal_triangle(n):
    """ This function returns int in list of lists [[<int>]] based on pascale rule of
    user inputs n.
    """
    output = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            lst = 1
            for j in range(1, i + 1):
                level.append(lst)
                lst = lst * (i - j) // j
            output.append(level)
    return output
