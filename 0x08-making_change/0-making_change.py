#!/usr/bin/python3

"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Change comes from within” project, you will tackle a classic problem from
    the domain of dynamic programming and greedy algorithms: the coin change
    problem. The objective is to find the minimum number of coins required
    to make up a given total amount, given a list of coin denominations
    This project challenges you to apply your understanding of algorithms
    to devise a solution that is not only correct but also efficient.
    Below are the key concepts and resources necessary to complete
    this project successfully
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for cn in coins:
        while cn <= total:
            total -= cn
            change += 1
        if (total == 0):
            return change
    return -1
