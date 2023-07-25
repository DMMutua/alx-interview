#!/usr/bin/python3
"""Dynamic Programming Approach to Minimum Operations"""


def minOperations(n: int) -> int:
    """
    Finds the Minimum number of Operations
    needed to get exactly n `H`
    characters in the file.
    """
    if n == 1:
        return 0

    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        # Initialize the current value as positive infinity
        dp[i] = float('inf')
        for j in range(1, i):
            if i % j == 0:
                # Update minimum operations
                dp[i] = min(dp[i], dp[j] + (i // j))

    return dp[n] if dp[n] != float('inf') else 0
