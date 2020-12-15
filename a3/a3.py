fin = open('a3.in')
grid = []
for line in fin.readlines():
    grid.append(line.strip())
fin.close()

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


ret = [
    check(1, 1, grid), 
    check(3, 1, grid), 
    check(5, 1, grid), 
    check(7, 1, grid), 
    check(1, 2, grid),
]
product = 1
for i in ret:
    product *= i
print(product, ret)