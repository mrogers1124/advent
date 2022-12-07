# Advent of Code 2022
# Day 06, Problem 1
# Author: Matt Rogers


import sys


# Main method
def main(raw: str) -> str:
    buffer = raw.strip()
    return str(find_marker(buffer, length=4))


def find_marker(buffer: str, length) -> int:
    for n in range(length, len(buffer)):
        if len(set(buffer[n-length:n])) == length:
            return n


if __name__ == '__main__':
    puzzle_input = sys.stdin.read()
    puzzle_output = main(puzzle_input)
    print(puzzle_output)
