fin = open('a20.in')
file = fin.read()
fin.close()

def rotate(x):
    return [[x[-(i+1)][j] for i in range(len(x))] for j in range(len(x))]

def flip(x):
    return [[x[j][-(i+1)] for i in range(len(x))] for j in range(len(x))]

class Tile:
    def __init__(self, tile, name):
        self.tile = tile
        self.name = name
        self.size = len(tile)
        self.neighbours = [None, None, None, None]

    def fit_up(self, tile):
        return self.get_up_edge() == tile.get_down_edge()

    def fit_right(self, tile):
        return self.get_right_edge() == tile.get_left_edge()

    def fit_down(self, tile):
        return tile.fit_up(self)

    def fit_left(self, tile):
        return tile.fit_right(self)

    def get_up_edge(self):
        return "".join(self.tile[0])

    def get_down_edge(self):
        return "".join(self.tile[-1])

    def get_right_edge(self):
        return "".join(self.tile[i][-1] for i in range(self.size))

    def get_left_edge(self):
        return "".join(self.tile[i][0] for i in range(self.size))

    def rotate(self):
        self.tile = rotate(self.tile)
        self.neighbours = [self.neighbours[-1]] + self.neighbours[:-1]

    def flip(self):
        self.tile = flip(self.tile)
        self.neighbours[1], self.neighbours[3] = self.neighbours[3], self.neighbours[1]

    def set_up(self, tile):
        self.neighbours[0] = tile

    def _align(self, tile, condition):
        for flips in range(2):
            for rotations in range(4):
                if condition(tile): return
                tile.rotate()
            tile.flip()

    def _get(self, idx, fit):
        tile = self.neighbours[idx]
        if tile == None: return tile
        self._align(tile, fit)
        return tile

    def get_up(self):
        return self._get(0, self.fit_up)

    def get_right(self):
        return self._get(1, self.fit_right)

    def get_down(self):
        return self._get(2, self.fit_down)

    def get_left(self):
        return self._get(3, self.fit_left)

    def is_corner(self):
        count = 0
        for tile in self.neighbours:
            if tile != None: count += 1
        return count == 2

    def make_top_left(self):
        if not self.is_corner(): return
        while self.get_up() != None or self.get_left() != None:
            self.rotate()
            
def find_monster(x, y):
    global image, grid
    points = [(0, 18), (1, 0), (1, 5), (1, 6), (1, 11), (1, 12), (1, 17), (1, 18), (1, 19), (2, 1), (2, 4), (2, 7), (2, 10), (2, 13), (2, 16)]
    count = 0
    for dx, dy in points:
        if image[dx + x][dy + y] == '#':
            count += 1
    if count == len(points):
        for dx, dy in points:
            grid[dx + x][dy + y] = 0
        return True
    return False

tiles_raw = file.split("\n\n")

tiles = {}
for tile in tiles_raw:
    tile = tile.split("\n")
    name = tile.pop(0)
    name = int(name.split(' ')[1][:-1])

    tile = Tile(list(map(list, tile)), name)
    tiles[name] = tile

for tile_a in tiles.values():
    for rotations in range(4):
        for tile_b in tiles.values():
            for flips in range(2):
                for rotations in range(4):
                    if tile_a.fit_up(tile_b):
                        tile_a.set_up(tile_b)
                    tile_b.rotate()
                tile_b.flip()
        tile_a.rotate()

count = 1
corners = []
for name in tiles:
    tile = tiles[name]
    if tile.is_corner():
        count *= name
        corners.append(tile)
print(count)

head = corners[0]
head.make_top_left()
image = []
count = 0
size = len(head.tile) - 2

while head != None:
    image += [row[1:-1] for row in head.tile[1:-1]]
    cur = head.get_right()
    while cur != None:
        tile = [row[1:-1] for row in cur.tile[1:-1]]
        for i in range(len(tile)):
            image[count + i] += tile[i]
        cur = cur.get_right()
    head = head.get_down()
    count += size

    
count = 0
grid = [[1 if image[j][i] == '#' else 0 for i in range(len(image))] for j in range(len(image))]
for flips in range(2):
    for rotations in range(4):
        for i in range(len(image) - 20):
            for j in range(len(image[i]) - 3):
                count += find_monster(j, i)
        if count > 0: break
        image = rotate(image)
        grid = rotate(grid)
    if count > 0: break
    image = flip(image)
    grid = flip(grid)
print(sum([sum(i) for i in grid]))
