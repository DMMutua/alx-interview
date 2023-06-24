# Island Perimeter
Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in grid:<br>
* `grid` is a list of list of integers;<br>
* In `grid`, 0 reps water, 1 reps land <br>
* In `grid` each Cell is square, with a side length of 1<br>
* Cells are Connected horizontally, Vertically and Not Diagonally<br>
* `grid` is rectangular, with its width and height not exceeding 100.
<br>

1. Grid is completely sorounded by water. There is only one island - or nothing.<br>
2. The Island doesn't have "lakes".

```
guillaume@ubuntu:~/0x09$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

guillaume@ubuntu:~/0x09$
guillaume@ubuntu:~/0x09$ ./0-main.py
12
guillaume@ubuntu:~/0x09$
```
