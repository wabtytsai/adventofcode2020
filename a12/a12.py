fin = open('a12.in')

def move_ship(lines):
    direction = 'E'
    horz = 0
    vert = 0
    actions = {
        'E': (1, 0),
        'W': (-1, 0),
        'N': (0, 1),
        'S': (0, -1),
        'R': 1,
        'L': -1,
    }
    change = "NESW"
    for line in lines:
        action = line[0]
        value = int(line[1:])
        
        if action in 'RL':
            idx = change.find(direction)
            sign = actions[action]
            direction = change[(idx + sign * (value // 90)) % len(change)]
            continue
        if action == 'F':
            x, y = actions[direction]
        else:
            x, y = actions[action]
        horz += x * value
        vert += y * value
    return (abs(horz) + abs(vert))

def move_waypoint(lines):
    horz = 0
    vert = 0
    way_x = 10
    way_y = 1
    actions = {
        'E': (1, 0),
        'W': (-1, 0),
        'N': (0, 1),
        'S': (0, -1),
        'R': (1, -1),
        'L': (-1, 1),
    }
    for line in lines:
        action = line[0]
        value = int(line[1:])
        
        if action in 'RL':
            x, y = actions[action]
            for i in range(value // 90):
                way_x, way_y = x * way_y, y * way_x
        elif action == 'F':
            horz += value * way_x
            vert += value * way_y
        else:
            x, y = actions[action]
            way_x += x * value
            way_y += y * value
    return (abs(horz) + abs(vert))

lines = fin.readlines()

print(move_ship(lines))
print(move_waypoint(lines))

fin.close()
