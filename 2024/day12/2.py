import sys

DEBUG = False

garden = [list(_) for _ in sys.stdin.read().strip().split("\n")]

if DEBUG:
    for row in garden:
        for plot in row:
            print(plot, end="")
        print()


plot_processed = [[False for _ in range(len(garden[0]))] for _ in range(len(garden))]


def is_processed(x, y):
    if x < 0 or x >= len(garden) or y < 0 or y >= len(garden[0]):
        return True
    return plot_processed[x][y]


def get_plant(x, y):
    if x < 0 or x >= len(garden) or y < 0 or y >= len(garden[0]):
        return None
    return garden[x][y]


def get_region(garden, x, y):
    plot_processed[x][y] = True
    area = 1
    perimeter = 0
    corners = 0
    edges = []
    plant = garden[x][y]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        if get_plant(x + dx, y + dy) == plant:
            if not is_processed(x + dx, y + dy):
                next_plot = get_region(garden, x + dx, y + dy)
                area += next_plot[0]
                perimeter += next_plot[1]
                corners += next_plot[2]
        else:
            perimeter += 1
            edges.append((dx, dy))
    if (0, 1) in edges:
        if (1, 0) in edges:
            corners += 1
            print(f"++ corner at {x}, {y}") if DEBUG else None
        if (-1, 0) in edges:
            corners += 1
            print(f"-+ corner at {x}, {y}") if DEBUG else None
    if (0, -1) in edges:
        if (1, 0) in edges:
            corners += 1
            print(f"+- corner at {x}, {y}") if DEBUG else None
        if (-1, 0) in edges:
            corners += 1
            print(f"-- corner at {x}, {y}") if DEBUG else None
    if (
        get_plant(x + 1, y + 1) != plant
        and get_plant(x, y + 1) == plant
        and get_plant(x + 1, y) == plant
    ):
        corners += 1
        print(f"++ concave corner at {x}, {y}") if DEBUG else None
    if (
        get_plant(x + 1, y - 1) != plant
        and get_plant(x, y - 1) == plant
        and get_plant(x + 1, y) == plant
    ):
        corners += 1
        print(f"+- concave corner at {x}, {y}") if DEBUG else None
    if (
        get_plant(x - 1, y + 1) != plant
        and get_plant(x, y + 1) == plant
        and get_plant(x - 1, y) == plant
    ):
        corners += 1
        print(f"-+ concave corner at {x}, {y}") if DEBUG else None
    if (
        get_plant(x - 1, y - 1) != plant
        and get_plant(x, y - 1) == plant
        and get_plant(x - 1, y) == plant
    ):
        corners += 1
        print(f"-- concave corner at {x}, {y}") if DEBUG else None

    return area, perimeter, corners


total_price = 0
for x, row in enumerate(garden):
    for y, plot in enumerate(row):
        if not plot_processed[x][y]:
            area, perimeter, corners = get_region(garden, x, y)
            (
                print(
                    f"A region of {get_plant(x, y)} with price "
                    + f"{area} * {corners} = {area * corners}"
                )
                if DEBUG
                else None
            )
            total_price += area * corners

print(total_price)
