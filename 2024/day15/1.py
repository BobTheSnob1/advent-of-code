import sys

DEBUG = False

input = sys.stdin.read().strip().split("\n\n")


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Warehouse:
    def __init__(self, data):
        self.warehouse = [list(_) for _ in data.split("\n")]
        self.width = len(self.warehouse[0])
        self.height = len(self.warehouse)
        self.robot = None
        for y, row in enumerate(self.warehouse):
            for x, cell in enumerate(row):
                if cell == "@":
                    self.robot = Robot(x, y)
                    break
        if not self.robot:
            raise ValueError("Robot not found")

    def __repr__(self):
        output = f"Warehouse with robot at {self.robot}:\n"
        for row in self.warehouse:
            output += "".join(row) + "\n"
        return output

    def gps_sum(self):
        sum = 0

        for y, row in enumerate(self.warehouse):
            for x, cell in enumerate(row):
                if cell == "O":
                    sum += (100 * y) + x
        return sum

    def move(self, direction):
        if move not in "^v<>":
            raise ValueError("Invalid move")
        match direction:
            case "^":
                direction = (0, -1)
                print("Moving up") if DEBUG else None
            case "v":
                direction = (0, 1)
                print("Moving down") if DEBUG else None
            case "<":
                direction = (-1, 0)
                print("Moving left") if DEBUG else None
            case ">":
                direction = (1, 0)
                print("Moving right") if DEBUG else None

        x = self.robot.x + direction[0]
        y = self.robot.y + direction[1]

        while self.warehouse[y][x] == "O":
            x += direction[0]
            y += direction[1]

        if self.warehouse[y][x] == "#":
            return False
        elif self.warehouse[y][x] == ".":
            self.warehouse[y][x] = "O"
            self.warehouse[self.robot.y][self.robot.x] = "."
            self.robot.x += direction[0]
            self.robot.y += direction[1]
            self.warehouse[self.robot.y][self.robot.x] = "@"
            return True


warehouse = Warehouse(input[0])
moves = [_ for _ in input[1] if _ != "\n"]

if DEBUG:
    print(warehouse)

    print("Moves:")
    for move in moves:
        print(move, end="")
    print()

for i, move in enumerate(moves):
    warehouse.move(move)
    if DEBUG:
        print(f"Move {i + 1}:")
        print(warehouse)

print("Final GPS Sum:") if DEBUG else None
print(warehouse.gps_sum())
