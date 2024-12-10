import sys
from copy import copy

DEBUG = False

input = sys.stdin.read().strip()

map = [[int(h) for h in _] for _ in input.split("\n")]
if DEBUG:
    for row in map:
        for h in row:
            print(h, end="")
        print()


def map_value(x, y):
    if 0 <= x < len(map) and 0 <= y < len(map[0]):
        return map[x][y]
    return -1


class Step:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = map[x][y]

    def __repr__(self):
        return f"Step at {self.x}, {self.y} with height {self.height}"


class Trail:
    def __init__(self, path: list):
        self.path = path

    def __repr__(self):
        return f"Trial with path {self.path}"

    def __hash__(self):
        return hash(str(self.path))

    def add_step(self, x, y):
        self.path.append(Step(x, y))


def get_unique_trails(map, trail):
    trails_found = set()
    height = trail.path[-1].height
    x, y = trail.path[-1].x, trail.path[-1].y
    if height == 9:
        trails_found.add(trail)
        return trails_found
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if map_value(nx, ny) == height + 1:
            new_trail = copy(trail)
            new_trail.add_step(nx, ny)
            trails_found.update(get_unique_trails(map, new_trail))
    return trails_found


sum_scores = 0

for x, row in enumerate(map):
    for y, height in enumerate(row):
        if map[x][y] == 0:
            unique_trails = len(get_unique_trails(map, Trail([Step(x, y)])))
            sum_scores += unique_trails


print(sum_scores)
