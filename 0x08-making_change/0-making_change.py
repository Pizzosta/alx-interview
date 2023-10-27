#!/usr/bin/python3
"""Making change effective"""


def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list of int): A list of coin denominations available.
        total (int): The target total amount to make change for.

    Returns:
        int: The fewest number of coins needed to meet the total.
             If the total cannot be reached using the
             sprovided coin denominations, returns -1.
    """
    if total <= 0:
        return 0
    table = [sys.maxsize for i in range(total + 1)]
    table[0] = 0
    m = len(coins)
    for i in range(1, total + 1):
        for j in range(m):
            if coins[j] <= i:
                subres = table[i - coins[j]]
                if subres != sys.maxsize and subres + 1 < table[i]:
                    table[i] = subres + 1

    if table[total] == sys.maxsize:
        return -1
    return table[total]
