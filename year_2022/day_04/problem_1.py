# Advent of Code 2022
# Day 04, Problem 1
# Author: Matt Rogers


import sys


# Main method
def main(raw: str) -> str:
    # Clean input stream
    data = raw.strip()
    containment_count = [check_containment(row) for row in data.split('\n')]
    return str(sum(containment_count))


def check_containment(row: str) -> int:
    ranges = [[int(n) for n in range.split('-')] for range in row.split(',')]
    if ranges[0][0] <= ranges[1][0] and ranges[0][1] >= ranges[1][1]:
        return 1
    if ranges[1][0] <= ranges[0][0] and ranges[1][1] >= ranges[0][1]:
        return 1
    return 0


if __name__ == '__main__':
    puzzle_input = sys.stdin.read()
    puzzle_output = main(puzzle_input)
    print(puzzle_output)
