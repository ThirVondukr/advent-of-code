import collections
import itertools
from typing import Iterable

BOARD_SIZE = 5


def split(iterable, separator):
    chunk = []
    for element in iterable:
        if element == separator:
            yield chunk
            chunk = []
            continue
        chunk.append(element)
    yield chunk


def board_lines(board: list[list[int]]) -> Iterable[list[int]]:
    for col in zip(*board):
        yield col
    for line in board:
        yield line


def parse_data():
    with open("inputs/day_4") as file:
        lines = file.readlines()

    cards = list(map(int, lines[0].split(",")))

    lines = (l.strip() for l in lines[1:])
    lines = (list(map(int, l.split())) or None for l in lines)
    boards: list[list[list[int]]] = list(split(lines, separator=None))
    return cards, boards


def winning_boards() -> tuple[list[list[int]], int, set[int]]:
    cards, boards = parse_data()
    boards = collections.deque(boards)
    chosen_cards = set()

    for card in cards:
        chosen_cards.add(card)
        processed_boards = []
        for board in boards:
            if any(all(number in chosen_cards for number in line) for line in board_lines(board)):
                yield board, card, chosen_cards.copy()
                # return sum(n for n in itertools.chain.from_iterable(board) if n not in chosen_cards) * card
            else:
                processed_boards.append(board)
        boards = processed_boards


def board_score(board, card, chosen_cards):
    return sum(n for n in itertools.chain.from_iterable(board) if n not in chosen_cards) * card


def part_one():
    board, card, chosen_cards = next(winning_boards())
    print(board_score(board, card, chosen_cards))


def part_two():
    board, card, chosen_cards = next(iter(collections.deque(winning_boards(), maxlen=1)))
    print(board_score(board, card, chosen_cards))


if __name__ == '__main__':
    part_one()
    part_two()
