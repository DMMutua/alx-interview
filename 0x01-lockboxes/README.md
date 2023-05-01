# LockBoxes Interview Question
You have `n` number of locked boxes in front of you. Each box is numbered sequentially from 0 to `n - 1` and each box may contain keys to the other boxes.
<br>
Write a method that determines if all the boxes can be opened.
* Prototype: `def canUnlockAll(boxes)`<br>
* `boxes` is a list of lists
* A Key with the same Number as a Box Opens that Box
* All Keys will be positive Integers
*         -> There Can Be Keys that do not have Boxes
* The first boz `boxes[0]` is unlocked
* Return `True` if all Boxes can be Opened, else return `False`
```
carrie@ubuntu:~/0x01-lockboxes$ cat main_0.py
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

carrie@ubuntu:~/0x01-lockboxes$
```
<br>

```
carrie@ubuntu:~/0x01-lockboxes$ ./main_0.py
True
True
False
carrie@ubuntu:~/0x01-lockboxes$
```
