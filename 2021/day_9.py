import dataclasses
import functools
import heapq
import operator
from typing import Iterable, NamedTuple


class Point(NamedTuple):
    value: int
    x: int
    y: int


@dataclasses.dataclass
class HeightMap:
    map: list[list[int]]
    dimensions: tuple[int, int]

    def __contains__(self, item: tuple[int, int]):
        size_x, size_y = self.dimensions
        x, y = item
        return x in range(size_x) and y in range(size_y)

    def __getitem__(self, item: tuple[int, int]):
        x, y = item
        return Point(value=self.map[y][x], x=x, y=y)

    def __iter__(self) -> Iterable[Point]:
        size_x, size_y = self.dimensions
        for x in range(size_x):
            for y in range(size_y):
                yield self[x, y]

    def adjacent_points(self, x: int, y: int) -> Iterable[Point]:
        locations = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
        ]
        for loc in locations:
            if loc in self:
                yield self[loc]

    def flow_points(self) -> Iterable[Point]:
        for point in self:
            if all(
                point.value < adj_point.value
                for adj_point in self.adjacent_points(point.x, point.y)
            ):
                yield point

    def basin(self, flow_point: Point) -> Iterable[Point]:
        seen: set[Point] = set()
        stack = [flow_point]

        while stack:
            point = stack.pop()
            if point in seen:
                continue

            seen.add(point)
            yield point

            for adj_point in self.adjacent_points(point.x, point.y):
                if adj_point.value == 9 or adj_point in seen:
                    continue

                if adj_point.value > point.value:
                    stack.append(adj_point)

    def basins(self) -> Iterable[list[Point]]:
        for point in self.flow_points():
            yield list(self.basin(point))


def read_heightmap() -> HeightMap:
    with open("inputs/day_9") as file:
        data = [l.strip() for l in file.readlines()]

    data = [
        list(map(int, line))
        for line in data
    ]
    x, y = len(data[0]), len(data)
    return HeightMap(
        map=data,
        dimensions=(x, y)
    )


def part_one():
    heightmap = read_heightmap()
    return sum(flow_point.value + 1 for flow_point in heightmap.flow_points())


def part_two():
    heightmap = read_heightmap()
    largest_3 = heapq.nlargest(
        3,
        heightmap.basins(),
        len,
    )
    print([(b[0], len(b)) for b in largest_3])
    return functools.reduce(operator.mul, map(len, largest_3))


if __name__ == "__main__":
    print(part_one())
    print(part_two())
