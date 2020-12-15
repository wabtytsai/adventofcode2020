# Day 3 
Day 3's part I and part II are the same problem, just with different parameters. We can combine them and come up with one solution for both parts.

We are given a 2D array which represents the map of the forest. We simply need to go from top to bottom, and in every step, we go right `x` number of times, and go down `y` number of times, and see if we encountered a tree or not. The one catch is:

> These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome stability, the same pattern repeats to the right many times

All of this blob of text just means the array wraps around horizontally. We can thus track the horizontal position by modding the value by the width of the forest.

```python
def check(right, down, grid):
    width = len(grid[0])
    height = len(grid)

    count = 0
    x = 0
    for y in range(0, height, down):
        if grid[y][x] == '#':
            count += 1
        x = (x + right) % width
    return count
```