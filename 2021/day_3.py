import operator
from typing import Literal


def find_most_common_bit(number: str | list[str]) -> 0 | 1:
    return int(number.count("1") >= number.count("0"))


def calculate_rating(numbers: list[str], find_common: Literal["most", "least"]) -> int:
    comparison_op = operator.eq if find_common == "most" else operator.ne

    for i in range(len(numbers[0])):
        column = [number[i] for number in numbers]
        most_common_bit = str(find_most_common_bit(column))
        numbers = [number for number in numbers if comparison_op(number[i], most_common_bit)]

        if len(numbers) == 1:
            break

    return int("".join(str(n) for n in numbers[0]), base=2)


def part_1():
    with open("inputs/day_3") as file:
        numbers = list(map(str.strip, file.readlines()))

    gamma = [find_most_common_bit(column) for column in zip(*numbers)]
    epsilon = [int(not n) for n in gamma]
    gamma = int("".join(map(str, gamma)), base=2)
    epsilon = int("".join(map(str, epsilon)), base=2)
    return gamma * epsilon


def part_2():
    with open("inputs/day_3") as file:
        numbers = list(map(str.strip, file.readlines()))

    o2 = calculate_rating(numbers, find_common="most")
    co2 = calculate_rating(numbers, find_common="least")
    return o2, co2, o2 * co2


if __name__ == '__main__':
    print(part_1())
    print(part_2())
