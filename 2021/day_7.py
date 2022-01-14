def fuel_cost_const(position: int, crab_positions: list[int]) -> int:
    return sum(abs(position - crab_position) for crab_position in crab_positions)


def fuel_cost_linear(position, crab_positions: list[int]) -> int:
    return sum(
        abs(position - crab_position) * (abs(position - crab_position) + 1) // 2
        for crab_position in crab_positions
    )


def main():
    with open("inputs/day_7") as file:
        crab_positions = list(map(int, file.readline().split(",")))
        # crab_positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

    min_cost_const = min(
        fuel_cost_const(pos, crab_positions)
        for pos in range(min(crab_positions), max(crab_positions) + 1)
    )
    min_cost_linear = min(
        fuel_cost_linear(pos, crab_positions)
        for pos in range(min(crab_positions), max(crab_positions) + 1)
    )
    return min_cost_const, min_cost_linear


if __name__ == '__main__':
    print(main())
