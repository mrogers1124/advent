# Advent of Code 2022
# Day 03, Problem 2
# Author: Matt Rogers


import sys
from typing import List


# Main method
def main(raw: str) -> str:
    # Clean input stream
    data = raw.strip()

    # Separate into rucksacks and three-elf groups
    rucksacks = data.split('\n')
    elfgroups = [rucksacks[3*i:3*i+3] for i in range(len(rucksacks) // 3)]

    # Find badges
    badges = [find_badges(elfgroup) for elfgroup in elfgroups]

    # Find the total priority of all the badges
    badge_priorities = [item_priority(badge) for badge in badges]
    priority = sum(badge_priorities)

    # Return the total priority
    return str(priority)


# Returns a string containing all items common in all rucksacks
def find_badges(elfgroup: List[str]) -> str:
    items = set(''.join(elfgroup))
    return ''.join([
        item for item in items
        if all([item in rucksack for rucksack in elfgroup])
    ])


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
