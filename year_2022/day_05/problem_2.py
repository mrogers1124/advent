# Advent of Code 2022
# Day 05, Problem 2
# Author: Matt Rogers


import sys
from typing import List


# Main method
def main(raw: str) -> str:
    stacks, instructions = parse_raw_data(raw)
    for count, from_index, to_index in instructions:
        picked_crates = stacks[from_index][-count:]
        stacks[to_index].extend(picked_crates)
        stacks[from_index] = stacks[from_index][:-count]

    solution = ''.join([stack[-1] for stack in stacks])
    return solution


def parse_raw_data(raw: str):
    stacks_raw, instructions_raw = raw.split('\n\n')

    # Transform the initial stack diagram
    # into a list of lists of characters
    stacks_raw_transpose = list(zip(*reversed(stacks_raw.split('\n'))))
    stacks = [
        [crate for crate in stack[1:] if crate != ' ']
        for stack in stacks_raw_transpose
        if stack[0] != ' '
    ]

    # Transform the instructions
    # into a list of tuples (count, from_index, to_index)
    # Note that the first stack labeled "1" in the diagram will have index 0
    instructions = [
        tuple([
            int(instruction.split(' ')[1]),
            int(instruction.split(' ')[3]) - 1,
            int(instruction.split(' ')[5]) - 1
        ])
        for instruction in instructions_raw.split('\n')
        if instruction != ''
    ]

    return stacks, instructions


if __name__ == '__main__':
    puzzle_input = sys.stdin.read()
    puzzle_output = main(puzzle_input)
    print(puzzle_output)
