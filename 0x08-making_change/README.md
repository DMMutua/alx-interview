# Dynamic Programming: Solving the Coins Problem
## Change Comes from Within
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount `total`.<br>
* Prototype: `def makeChange(coins, total)`<br>
* Return: fewest number of coins needed to meet `total`
*   * if `total` is `0` or Less, return `0`
*   * If `total` cannot be met by any number of coins you have, return `-1`
* `coins` is a list of the values of the coins in your possession.
* The Value of a coin will always be an integer greater than `0`.
* You can assume you Infinite number of each coin denomination.
* Solution's Runtime is Measured <br>

```
carrie@ubuntu:~/0x08-making_change$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

carrie@ubuntu:~/0x08-making_change$
```

<br> Solution:
```
carrie@ubuntu:~/0x08-making_change$ ./0-main.py
7
-1
carrie@ubuntu:~/0x08-making_change$
```
