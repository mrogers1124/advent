# Advent of Code 2022
# Day 01, Problem 1
# Author: Matt Rogers

import sys


def main(raw: str) -> str:
    # Clean the input data
    input_string = raw.strip()

    # Split elf inventories by double newlines
    # Split items in inventories by single newlines
    inventories = [inventory.split('\n') for inventory in input_string.split('\n\n')]

    # Convert data type & aggregate total calories by elf
    calories = [[int(item) for item in inventory] for inventory in inventories]
    calorie_totals = [sum(item) for item in calories]

    # Return the maximum calorie total
    return str(max(calorie_totals))


if __name__ == '__main__':
    puzzle_input = sys.stdin.read().strip()
    puzzle_output = main(puzzle_input)
    print(puzzle_output)
