fin = open('a17.in')
lines = fin.readlines()
fin.close()
lines = [line.strip() for line in lines]

space = dict()

for y in range(len(lines)):
    for x in range(len(lines[0])):
        space[(x, y, 0, 0)] = lines[y][x] == '#'

def next_state(point):
    global space
    count = 0
    for n in neighbours(point):
        count += space.get(n, False)
    if space.get(point, False):
        return count == 2 or count == 3
    else:
        return count == 3

def neighbours(p):
    delta = (-1, 0, 1)
    for dx in delta:
        for dy in delta:
            for dz in delta:
                for dw in delta:
                    if dx == dy == dz == dw == 0: continue
                    yield p[0] + dx, p[1] + dy, p[2] + dz, p[3] + dw

cycles = 6
for i in range(cycles):
    new_space = dict()
    count = 0
    for point in {point for key in space.keys() for point in neighbours(key)}:
        state = next_state(point)
        new_space[point] = state
        count += state
    space = new_space
print(count)


