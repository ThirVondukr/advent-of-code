import collections


def read_input() -> dict[int, int]:
    with open("inputs/day_6") as file:
        values = map(int, file.read().split(","))
    counter = collections.defaultdict(int)
    for k, v in collections.Counter(values).items():
        counter[k] = v
    return counter


def simulate(days: int):
    fish = read_input()
    for _ in range(days):
        new_fish_amount, fish[0] = fish[0], 0
        for i in range(1, 8 + 1):
            fish[i - 1] = fish[i]
        fish[6] += new_fish_amount
        fish[8] = new_fish_amount
    return sum(fish.values())


if __name__ == '__main__':
    print(simulate(days=80))
    print(simulate(days=256))
