def main() -> tuple[int, int]:
    with open("inputs/day_2") as file:
        commands = file.readlines()

    aim = 0
    x, y = 0, 0
    for command in commands:
        command, value = command.split()
        value = int(value)

        if command == "down":
            aim += value
        elif command == "up":
            aim -= value
        else:
            x += value
            y += aim * value
    return x, y


if __name__ == '__main__':
    x, y = main()
    print(x * y)
