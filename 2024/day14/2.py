import sys
from PIL import Image

DEBUG = False

input = sys.stdin.read().strip().split("\n")


grid_dimensions = [101, 103]
if DEBUG:
    grid_dimensions = [11, 7]


class Robot:
    def __init__(self, data):
        data = data.split()
        self.position = list(map(int, data[0].split("=")[1].split(",")))
        self.velocity = list(map(int, data[1].split("=")[1].split(",")))

    def __repr__(self):
        return f"Robot at {self.position} with velocity {self.velocity}"

    def move(self, seconds=1):
        for _ in range(seconds):
            x = (self.position[0] + self.velocity[0]) % grid_dimensions[0]
            y = (self.position[1] + self.velocity[1]) % grid_dimensions[1]
            self.position = [x, y]

    def quadrant(self):
        if self.position[0] < grid_dimensions[0] // 2:
            if self.position[1] < grid_dimensions[1] // 2:
                return 0
            elif self.position[1] > grid_dimensions[1] // 2:
                return 1
        elif self.position[0] > grid_dimensions[0] // 2:
            if self.position[1] < grid_dimensions[1] // 2:
                return 2
            elif self.position[1] > grid_dimensions[1] // 2:
                return 3
        return 4


robots = [Robot(x) for x in input]

quadrants = [0, 0, 0, 0, 0]

final_positions = [
    [0 for _ in range(grid_dimensions[1])] for _ in range(grid_dimensions[0])
]


def save_grid(grid):
    height = len(grid)
    width = len(grid[0])
    image = Image.new("1", (width, height))  # "1" for 1-bit pixels, black and white
    pixels = image.load()

    for y in range(height):
        for x in range(width):
            pixels[x, y] = 0 if grid[y][x] > 0 else 1  # 0 is black, 1 is white

    image.save(f"images/grid_{_}.png")


safety_factor = [0 for _ in range(100)]
for _ in range(100):
    positions = [
        [0 for _ in range(grid_dimensions[1])] for _ in range(grid_dimensions[0])
    ]
    quadrants = [0, 0, 0, 0, 0]

    for robot in robots:
        robot.move()
        positions[robot.position[0]][robot.position[1]] += 1
        quadrants[robot.quadrant()] += 1
    print("Grid at second", _)
    safety_factor[_] = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
    save_grid(positions)


import matplotlib.pyplot as plt

plt.plot(safety_factor)
plt.xlabel("Time (seconds)")
plt.ylabel("Safety Factor")
plt.title("Safety Factor Over Time")
plt.savefig("images/safety_factor_plot.png")

if DEBUG:
    print(f"Quadrants: {quadrants}")
    print()
    for i, row in enumerate(final_positions):
        if i == len(final_positions) // 2:
            print()
            continue
        for j, cell in enumerate(row):
            if j == len(row) // 2:
                print(" ", end=" ")
                continue
            print(cell, end=" ") if cell > 0 else print(".", end=" ")
        print()
