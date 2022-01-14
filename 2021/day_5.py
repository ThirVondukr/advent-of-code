import collections
import math
from typing import NamedTuple, Iterable


class Point(NamedTuple):
    x: int
    y: int


def read_pipes() -> list[tuple[Point, Point]]:
    with open("inputs/day_5") as file:
        lines = file.readlines()
    pipes = []
    for line in lines:
        start, end = line.strip().split(" -> ")
        pipes.append(
            (
                Point(*map(int, start.split(","))),
                Point(*map(int, end.split(","))),
            )
        )
    return pipes


def is_diagonal(pipe):
    start, end = pipe
    return start[0] != end[0] and start[1] != end[1]


def points(a: Point, b: Point) -> Iterable[Point]:
    if a.x == b.x:
        x = a.x
        for y in range(min(a.y, b.y), max(a.y, b.y) + 1):
            yield Point(x, y)

    elif a.y == b.y:
        y = a.y
        for x in range(min(a.x, b.x), max(a.x, b.x) + 1):
            yield Point(x, y)
    else:
        delta_x = int(math.copysign(1, b.x - a.x))
        delta_y = int(math.copysign(1, b.y - a.y))
        x, y = a
        for _ in range(abs(a.x - b.x) + 1):
            yield Point(x, y)
            x += delta_x
            y += delta_y


def part_one():
    pipes = list(pipe for pipe in read_pipes() if not is_diagonal(pipe))
    pipes_map: dict[tuple[int, int], int] = collections.defaultdict(int)

    for pipe in pipes:
        start, end = pipe
        for point in points(start, end):
            pipes_map[point] += 1

    print(sum(1 for value in pipes_map.values() if value >= 2))


def part_two():
    pipes = read_pipes()
    pipes_map: dict[tuple[int, int], int] = collections.defaultdict(int)

    for pipe in pipes:
        start, end = pipe
        for point in points(start, end):
            pipes_map[point] += 1

    print(sum(1 for value in pipes_map.values() if value >= 2))


if __name__ == '__main__':
    # part_one()
    part_two()
