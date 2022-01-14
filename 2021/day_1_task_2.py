import itertools
from typing import Iterable


def sliding_window(iterable: Iterable[int], size: int) -> Iterable[list[int]]:
    iterator = iter(iterable)
    window = []
    for _ in range(size - 1):
        window.append(next(iterator))

    for value in iterator:
        window.append(value)
        yield tuple(window)
        del window[0]


def main():
    with open("inputs/day_1") as file:
        measurements = list(map(int, file.readlines()))

    return sum(
        1 for window1, window2 in itertools.pairwise(sliding_window(measurements, size=3))
        if sum(window2) > sum(window1)
    )


if __name__ == '__main__':
    print(main())
