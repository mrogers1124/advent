# Advent of Code 2022
# Day 04, Problem 2
# Author: Matt Rogers


import sys


# Main method
def main(raw: str) -> str:
    # Clean input stream
    data = raw.strip()
    overlap_count = [check_overlap(row) for row in data.split('\n')]
    return str(sum(overlap_count))


def check_overlap(row: str) -> int:
    ranges = [[int(n) for n in range.split('-')] for range in row.split(',')]
    return 0 if ranges[0][1] < ranges[1][0] or ranges[1][1] < ranges[0][0] else 1


if __name__ == '__main__':
    puzzle_input = sys.stdin.read()
    puzzle_output = main(puzzle_input)
    print(puzzle_output)
