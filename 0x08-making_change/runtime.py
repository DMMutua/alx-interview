#!/usr/bin/python3

import timeit
makeChange = __import__('0-making_change').makeChange

coins = [1, 2, 25]
total = 37

# Measure the runtime of makeChange function
runtime = timeit.timeit(lambda: makeChange(coins, total), number=1)

# Print the runtime
print("Runtime:", runtime, "seconds")
