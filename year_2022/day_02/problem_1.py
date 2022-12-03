# Advent of Code 2022
# Day 02, Problem 1
# Author: Matt Rogers

import sys
from typing import Tuple


# Declare constants
THROW_ROCK = 0
THROW_PAPER = 1
THROW_SCISSORS = 2

RESULT_DRAW = 0
RESULT_LOSE = 1
RESULT_WIN = 2

# Scores for lose, draw, and win
SCORE = {RESULT_LOSE: 0, RESULT_DRAW: 3, RESULT_WIN: 6}


# Decide the winner of a match
def decide_winner(elf_throw: int, my_throw: int) -> int:
    return (elf_throw - my_throw) % 3


# Parse the code for rock, paper, scissors throws
parse_letters = {'A': THROW_ROCK, 'B': THROW_PAPER, 'C': THROW_SCISSORS,
                 'X': THROW_ROCK, 'Y': THROW_PAPER, 'Z': THROW_SCISSORS}


# Parse a row of the input data
def parse_row(row: str) -> Tuple[int, int]:
    return parse_letters[row[0]], parse_letters[row[2]]


# Score a row of the input data
def score_row(row: str) -> int:
    elf_throw, my_throw = parse_row(row)
    result = decide_winner(elf_throw, my_throw)
    score = (my_throw + 1) + SCORE[result]
    return score


# Main method
def main(raw: str) -> str:
    # Clean the input data
    data = raw.strip()

    # Compute the score
    score = sum([score_row(row) for row in data.split('\n')])
    return str(score)


if __name__ == '__main__':
    puzzle_input = sys.stdin.read()
    puzzle_output = main(puzzle_input)
    print(puzzle_output)
