import sys
from PIL import Image
import numpy as np

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

import matplotlib.pyplot as plt


def compute_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)


variances = []

for t in range(10000):
    x_positions = []
    y_positions = []

    for robot in robots:
        robot.move()
        x_positions.append(robot.position[0])
        y_positions.append(robot.position[1])

    x_variance = compute_variance(x_positions)
    y_variance = compute_variance(y_positions)
    product_variance = x_variance * y_variance
    variances.append((t, product_variance))

# Find the time with the lowest product variance
min_time, min_variance = min(variances, key=lambda x: x[1])
print(min_time + 1)

# Plot the product variance over time
times, product_variances = zip(*variances)
plt.plot(times, product_variances)
plt.xlabel("Time (seconds)")
plt.ylabel("Product of Variances")
plt.title("Product of Variances of Bot Positions Over Time")
plt.show()

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
