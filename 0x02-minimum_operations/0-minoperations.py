#!/usr/bin/python3
""" This is an app for Algorithm in python.
"""


def minOperations(n):
    """ This func will calc the fewest number of operations needed to result
    in exactly n H characters in the file.
    Prototype: def minOperations(n)
    -- Returns an integer
    and If n is impossible to achieve, return 0
    """

    if (n < 2):
        return 0
    res, base = 0, 2
    while base <= n:
        if n % base == 0:
            res += base
            n = n / base
            base -= 1
        base += 1
    return res
