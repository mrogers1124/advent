# Advent of Code 2022
# Day 03, Problem 1
# Author: Matt Rogers


import sys


# Main method
def main(raw: str) -> str:
    # Clean input stream
    data = raw.strip()

    # Separate into rucksacks
    rucksacks = data.split('\n')

    # Find common items
    common_items = [find_common_items(rucksack) for rucksack in rucksacks]

    # Find the total priority of all the common items
    common_item_priorities = [item_priority(item) for item in common_items]
    priority = sum(common_item_priorities)

    # Return the total priority
    return str(priority)


# Returns a string containing all items common in both compartments
def find_common_items(rucksack: str) -> str:
    n = len(rucksack) // 2
    return ''.join(
        [char for char in set(rucksack)
         if char in rucksack[:n]
         and char in rucksack[n:]]
    )


# Calculate priority of an item
def item_priority(item: str) -> int:
    n = ord(item)
    if n >= ord('a'):
        return n - (ord('a') - 1)
    else:
        return n - (ord('A') - 1) + 26


if __name__ == '__main__':
    puzzle_input = sys.stdin.read()
    puzzle_output = main(puzzle_input)
    print(puzzle_output)
