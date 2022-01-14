from __future__ import annotations

import dataclasses
import itertools
from typing import Iterable, Optional


@dataclasses.dataclass
class Display:
    inputs: tuple[set[str], ...]
    outputs: tuple[set[str], ...]
    mapping: dict[int, Optional[set[str]]] = dataclasses.field(
        default_factory=lambda: dict.fromkeys(range(0, 9 + 1), None)
    )

    @classmethod
    def from_line(cls, line: str) -> Display:
        inputs, outputs = (part.strip().split(" ") for part in line.split(" | "))
        return cls(
            inputs=tuple(map(set, inputs)),
            outputs=tuple(map(set, outputs))
        )

    def digit_value(self, str_: str) -> int:
        return next(k for k, v in self.mapping.items() if v == set(str_))

    @property
    def all_digits(self) -> Iterable[set[str]]:
        yield from self.inputs
        yield from self.outputs

    @property
    def unassigned_digits(self):
        return (d for d in self.all_digits if d not in self.mapping.values())

    @property
    def output_value(self):
        number = "".join(str(self.digit_value("".join(output))) for output in self.outputs)
        return int(number)


def part_one():
    with open("inputs/day_8") as file:
        outputs = [
            line.split(" | ")[1].strip().split(" ")
            for line in file.readlines()
        ]
    return sum(
        1 for digit in itertools.chain.from_iterable(outputs)
        if len(digit) in {2, 4, 3, 7}
    )


def assign_digit(
    display: Display,
    digit: int,
    superset_of: Optional[int] = None,
    len_constraint: Optional[int] = None,
) -> None:
    gen = display.unassigned_digits
    if superset_of is not None:
        gen = (d for d in gen if d.issuperset(display.mapping[superset_of]))
    if len_constraint is not None:
        gen = (d for d in gen if len(d) == len_constraint)
    display.mapping[digit] = next(gen)


def part_two():
    with open("inputs/day_8") as file:
        displays = [Display.from_line(line) for line in file.readlines()]

    identifiable_digits = {
        1: 2,
        4: 4,
        7: 3,
        8: 7,
    }
    sum_ = 0
    for display in displays:
        for digit, digit_len in identifiable_digits.items():
            display.mapping[digit] = next(d for d in display.unassigned_digits if len(d) == digit_len)

        assign_digit(display, 3, 7, len_constraint=5)
        assign_digit(display, 9, 3)
        assign_digit(display, 0, 7)
        assign_digit(display, 6, len_constraint=6)
        display.mapping[2] = next(
            d for d in display.all_digits
            if len(set(d).intersection(set(display.mapping[4]))) == 2
            and d not in display.mapping.values()
        )
        assign_digit(display, 5)
        sum_ += display.output_value
    return sum_


if __name__ == '__main__':
    print(part_one())
    print(part_two())
