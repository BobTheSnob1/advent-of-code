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
    plant = garden[x][y]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dx, dy in directions:
        if get_plant(x + dx, y + dy) == plant:
            if not is_processed(x + dx, y + dy):
                next_plot = get_region(garden, x + dx, y + dy)
                area += next_plot[0]
                perimeter += next_plot[1]
        else:
            perimeter += 1
    return area, perimeter


total_price = 0
for x, row in enumerate(garden):
    for y, plot in enumerate(row):
        if not plot_processed[x][y]:
            area, perimeter = get_region(garden, x, y)
            (
                print(
                    f"A region of {get_plant(x, y)} with price "
                    + f"{area} * {perimeter} = {area * perimeter}"
                )
                if DEBUG
                else None
            )
            total_price += area * perimeter

print(total_price)
