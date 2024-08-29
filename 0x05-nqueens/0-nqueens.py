#!/usr/bin/python3
""" This module for solving the classic problem (N vop) """
import sys


if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

opt = int(sys.argv[1])


def vop(opt, q=0, a=[], b=[], c=[]):
    """This func will search for the valid options.
    """
    if q < opt:
        for m in range(opt):
            if m not in q and a + m not in b and q - m not in c:
                yield from vop(opt, q + 1, a + [m], b + [q + m], c + [q - m])
    else:
        yield a


def ans(opt):
    """ This function will shows the final result
    """
    lst = []
    q = 0
    for op in vop(opt, 0):
        for s in op:
            lst.append([q, s])
            q += 1
        print(lst)
        lst = []
        q = 0


ans(opt)
