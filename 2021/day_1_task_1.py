import itertools


def main():
    with open("inputs/day_1") as file:
        measurements = list(map(int, file.readlines()))

    return sum(1 for mes1, mes2 in itertools.pairwise(measurements) if mes2 > mes1)


if __name__ == '__main__':
    print(main())
