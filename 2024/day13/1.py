import sys
import math

DEBUG = False

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
        self.a = [a_x, a_y]
        self.b = [b_x, b_y]
        self.p = [p_x, p_y]
        self.position = [x, y]
        self.optimal_direction = (
            self.a
            if distance(self.p[0], self.p[1], self.a[0], self.a[1])
            < distance(self.p[0], self.p[1], self.b[0], self.b[1])
            else self.b
        )
        self.price = 0

    def __repr__(self):
        return (
            f"Button A: X+{self.a[0]}, Y+{self.a[1]}\n"
            f"Button B: X+{self.b[0]}, Y+{self.b[1]}\n"
            f"Prize: X={self.p[0]}, Y={self.p[1]}"
        )

    def move_hand(self, hand):
        if hand == "a":
            self.position[0] += self.a[0]
            self.position[1] += self.a[1]
            self.price += 3
        elif hand == "b":
            self.position[0] += self.b[0]
            self.position[1] += self.b[1]
            self.price += 1
        else:
            raise ValueError(f"Unknown hand: {hand}")

    def bigger_hand(self):
        if self.a[0] > self.b[0]:
            return "a"
        else:
            return "b"

    def move_to_prize(self):
        while True:
            if self.position == self.p:
                return
            elif self.position[0] > self.p[0] or self.position[1] > self.p[1]:
                self.price = -1
                return
            if intersects(*self.position, *self.a, *self.p) and intersects(
                *self.position, *self.b, *self.p
            ):
                self.move_hand(self.bigger_hand())
            elif intersects(*self.position, *self.a, *self.p):
                self.move_hand("a")
            else:
                self.move_hand("b")


games = [Game(game) for game in input.split("\n\n")]


if DEBUG:
    for game in games:
        print(game)
        print()


total_cost = 0
for i, game in enumerate(games):
    game.move_to_prize()
    if game.price > 0:
        total_cost += game.price
        print(f"Game {i+1} possible with price {game.price}") if DEBUG else None
    else:
        print(f"Game {i+1} impossible") if DEBUG else None

print(total_cost)
