import sys
import math

DEBUG = True

input = sys.stdin.read().strip()


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def intersects(x, y, dx, dy, target_x, target_y):
    while True:
        if x == target_x and y == target_y:
            return True
        if x > target_x or y > target_y:
            return False
        x += dx
        y += dy


class Game:
    def __init__(self, data):
        lines = data.strip().split("\n")
        button_a = lines[0].split(":")[1].strip().split(",")
        button_b = lines[1].split(":")[1].strip().split(",")
        prize = lines[2].split(":")[1].strip().split(",")
        a_x = int(button_a[0].strip().split("+")[1])
        a_y = int(button_a[1].strip().split("+")[1])
        b_x = int(button_b[0].strip().split("+")[1])
        b_y = int(button_b[1].strip().split("+")[1])
        p_x = int(prize[0].strip().split("=")[1])
        p_y = int(prize[1].strip().split("=")[1])
        x = 0
        y = 0
        self.a = (a_x, a_y)
        self.b = (b_x, b_y)
        self.p = (p_x, p_y)
        self.position = (x, y)
        self.optimal_direction = (
            self.a
            if distance(*self.p, *self.a) < distance(*self.p, *self.b)
            else self.b
        )

    def __repr__(self):
        return (
            f"Button A: X+{self.a[0]}, Y+{self.a[1]}\n"
            f"Button B: X+{self.b[0]}, Y+{self.b[1]}\n"
            f"Prize: X={self.p[0]}, Y={self.p[1]}"
        )

    def move_hand(self, hand):
        if hand == "a":
            self.pos[0] += self.a[0]
            self.pos[1] += self.a[1]
        elif hand == "b":
            self.pos[0] += self.b[0]
            self.pos[1] += self.b[1]
        else:
            raise ValueError(f"Unknown hand: {hand}")

    def optimal_hand(self):
        if intersects(self.x, self.y, self.a_x, self.a_y, self.p_x, self.p_y):
            return "a"


games = [Game(game) for game in input.split("\n\n")]


if DEBUG:
    for game in games:
        print(game)
        print()
