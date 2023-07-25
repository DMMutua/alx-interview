# Minimum Operations
In a Text File, there is a single character `H`.<br>
Your Text editor can execute only two operations in this file: `Copy All` and `Paste`. <br>
Given a Number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n``H` characters in the file.<br>
* Prototype: `def minOperations(n)`<br>
* Returns an Integer.
* if `n` is impossible to achieve, return `0`.<br>
example:
```
n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
```
<br>
```
carrie@ubuntu:~/0x02-minoperations$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

carrie@ubuntu:~/0x02-minoperations$
```
<br>
```
carrie@ubuntu:~/0x02-minoperations$ ./0-main.py
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
carrie@ubuntu:~/0x02-minoperations$
```
