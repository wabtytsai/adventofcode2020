fin = open('a3.in')
grid = []
for line in fin.readlines():
    grid.append(line.strip())

def check(down, right, grid):
    width = len(grid[0])
    height = len(grid)
    count = 0
    x = 0

    for i in range(0, height, down):
        if (grid[i][x] == '#'):
            count += 1
        x = (x + right) % width
    return count


ret = [check(1, 1, grid), check(1, 3, grid), check(1, 5, grid), check(1, 7, grid), check(2, 1, grid)]
product = 1
for i in ret:
    product *= i
print(product, ret)
fin.close()