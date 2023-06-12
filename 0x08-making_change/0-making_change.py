#!/usr/bin/python3
"""A Script to make change"""

from typing import List
import sys


def makeChange(coins: List[int], total: int) -> int:
    """Determines the fewest number of coins needed to meet
    a given amount of `total`
    Returns:
        - 0 if `total` is 0 or less
        - -1 if `total` can not be met by any number
            of coins in possesion.
    """
    if total <= 0:
        return 0

    arr = [float('inf')] * (total + 1)
    arr[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            arr[i] = min(arr[i], 1 + arr[i - coin])

    if arr[total] == float('inf'):
        return -1
    else:
        return arr[total]
