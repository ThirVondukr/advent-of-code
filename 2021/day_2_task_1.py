import enum


class Command(enum.Enum):
    forward = 1, 0
    down = 0, 1
    up = 0, -1


def main() -> int:
    with open("inputs/day_2") as file:
        commands = file.readlines()

    x, y = 0, 0
    for command in commands:
        command, value = command.split()
        value = int(value)

        vec_x, vec_y = Command[command].value
        x += vec_x * value
        y += vec_y * value
    return x * y


if __name__ == '__main__':
    print(main())
