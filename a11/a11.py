fin = open('a11.in')

def check(grid, x, y, state):
	count = 0
	for y2 in range(y - 1, y + 2):
		for x2 in range(x - 1, x + 2):
			if x2 == x and y2 == y: continue
			if not in_range(grid, x2, y2): continue
			count += grid[y2][x2] == state
	return count

def in_range(grid, x, y):
	return 0 <= y < len(grid) and 0 <= x < len(grid[0])

def shift(grid):
	new_grid = [[0] * len(grid[0]) for i in range(len(grid))]
	has_changed = False
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			state = grid[y][x]
			new_grid[y][x] = state
			if state == 'L':
				count = check(grid, x, y, '#')
				if count == 0:
					new_grid[y][x] = '#'
					has_changed = True
			elif state == '#':
				count = check(grid, x, y, '#')
				if count >= 4:
					new_grid[y][x] = 'L'
					has_changed = True
	return new_grid, has_changed

def check2(grid, x, y, state):
	count = 0
	# left
	for x2 in range(x - 1, -1, -1):
		if grid[y][x2] == '.': continue
		count += grid[y][x2] == state
		break
	# right
	for x2 in range(x + 1, len(grid[0])):
		if grid[y][x2] == '.': continue
		count += grid[y][x2] == state
		break
	# up
	for y2 in range(y - 1, -1, -1):
		if grid[y2][x] == '.': continue
		count += grid[y2][x] == state
		break
	# down
	for y2  in range(y + 1, len(grid)):
		if grid[y2][x] == '.': continue
		count += grid[y2][x] == state
		break
	# bottom-right
	for offset in range(len(grid)):
		x2 = x + offset
		y2 = y + offset
		if x2 == x and y2 == y: continue
		if not in_range(grid, x2, y2): break
		if grid[y2][x2] == '.': continue
		count += grid[y2][x2] == state
		break
	# top-right
	for offset in range(len(grid)):
		x2 = x + offset
		y2 = y - offset
		if x2 == x and y2 == y: continue
		if not in_range(grid, x2, y2): break
		if grid[y2][x2] == '.': continue
		count += grid[y2][x2] == state
		break
	# bottom-left
	for offset in range(len(grid)):
		x2 = x - offset
		y2 = y + offset
		if x2 == x and y2 == y: continue
		if not in_range(grid, x2, y2): break
		if grid[y2][x2] == '.': continue
		count += grid[y2][x2] == state
		break
	# top-left
	for offset in range(len(grid)):
		x2 = x - offset
		y2 = y - offset
		if x2 == x and y2 == y: continue
		if not in_range(grid, x2, y2): break
		if grid[y2][x2] == '.': continue
		count += grid[y2][x2] == state
		break
	return count

def shift2(grid):
	new_grid = [[0] * len(grid[0]) for i in range(len(grid))]
	has_changed = False
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			state = grid[y][x]
			new_grid[y][x] = state
			if state == 'L':
				count = check2(grid, x, y, '#')
				if count == 0:
					new_grid[y][x] = '#'
					has_changed = True
			elif state == '#':
				count = check2(grid, x, y, '#')
				if count >= 5:
					new_grid[y][x] = 'L'
					has_changed = True
	return new_grid, has_changed


grid = []
grid2 = []
for i in fin.readlines():
	grid.append(i.strip())
	grid2.append(i.strip())

has_changed = True
while has_changed:
	grid, has_changed = shift(grid)
count = 0
for i in grid:
	for j in i:
		if j == '#': count += 1
print(count)

has_changed = True
while has_changed:
	grid2, has_changed = shift2(grid2)
count = 0
for i in grid2:
	for j in i:
		if j == '#': count += 1
print(count)


fin.close()