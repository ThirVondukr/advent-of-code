from collections import defaultdict

CORRUPTED_POINTS_MAP = {
    "(": 3,
    "[": 57,
    "{": 1197,
    "<": 25137,
}
INCOMPLETE_POINTS_MAP = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}

OPEN_BRACKETS = set(CORRUPTED_POINTS_MAP)
BRACKETS_MAP = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}


def read_lines() -> list[str]:
    with open("inputs/day_10") as file:
        return [l.strip() for l in file.readlines()]


def corrupted_line_score(line: str) -> int:
    brackets: list[str] = []
    for bracket in line:
        if bracket in OPEN_BRACKETS:
            brackets.append(bracket)
        else:
            opening_bracket = BRACKETS_MAP[bracket]
            if brackets[-1] != opening_bracket:
                return CORRUPTED_POINTS_MAP[opening_bracket]
            brackets.pop()
    return 0


def incomplete_line_score(line: str) -> int:
    score = 0
    brackets_count = defaultdict(int)
    for bracket in reversed(line):
        if bracket in OPEN_BRACKETS:
            if brackets_count[bracket] == 0:
                score *= 5
                score += INCOMPLETE_POINTS_MAP[bracket]
            else:
                brackets_count[bracket] -= 1
        else:
            brackets_count[BRACKETS_MAP[bracket]] += 1

    return score


def incomplete_line_scores():
    for line in read_lines():
        if corrupted_line_score(line):
            continue
        yield incomplete_line_score(line)


def part_one():
    return sum(corrupted_line_score(line) for line in read_lines())


def part_two():
    scores = sorted(incomplete_line_scores())
    return scores[len(scores) // 2]


if __name__ == "__main__":
    print(part_one())
    print(part_two())
