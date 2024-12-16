import sys
import math
from fractions import Fraction


DEBUG = True
offset = 10000000000000

input = sys.stdin.read().strip()


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


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
        p_x = int(prize[0].strip().split("=")[1]) + offset
        p_y = int(prize[1].strip().split("=")[1]) + offset
        self.a = [a_x, a_y]
        self.b = [b_x, b_y]
        self.p = [p_x, p_y]

    def __repr__(self):
        return (
            f"Button A: X+{self.a[0]}, Y+{self.a[1]}\n"
            f"Button B: X+{self.b[0]}, Y+{self.b[1]}\n"
            f"Prize: X={self.p[0]}, Y={self.p[1]}"
        )

    def get_price(self):
        # Convert all values to fractions
        a_x, a_y = map(Fraction, self.a)
        b_x, b_y = map(Fraction, self.b)
        p_x, p_y = map(Fraction, self.p)

        determinant = a_x * b_y - a_y * b_x

        a_presses = (p_x * b_y - p_y * b_x) / determinant
        b_presses = (a_x * p_y - a_y * p_x) / determinant

        if DEBUG:
            print(f"Solution: ({a_presses}, {b_presses})")

        # Check if the solution values are integers
        if not a_presses.denominator == 1:
            print(f"A presses are not an integer: {a_presses}") if DEBUG else None
            return -1
        if not b_presses.denominator == 1:
            print(f"B presses are not an integer: {b_presses}") if DEBUG else None
            return -1

        if a_presses < 0:
            print(f"A presses are negative: {a_presses}") if DEBUG else None
            return -1
        if b_presses < 0:
            print(f"B presses are negative: {b_presses}") if DEBUG else None
            return -1

        return a_presses + (b_presses * 3)


games = [Game(game) for game in input.split("\n\n")]


if DEBUG:
    for game in games:
        print(game)
        print()


total_cost = 0
for i, game in enumerate(games):
    price = game.get_price()
    if price > 0:
        total_cost += price
        print(f"Game {i+1} possible with price {price}") if DEBUG else None
    else:
        print(f"Game {i+1} impossible") if DEBUG else None
    print() if DEBUG else None

print(total_cost)
