import re

INPUT_FILENAME = "input.txt"

def part_one():
    f = open(INPUT_FILENAME, "r")
    pattern = r"mul\((\d+),(\d+)\)"
    total = 0
    for line in f:
       for match in re.findall(pattern, line):
            total += int(match[0]) * int(match[1])
    print(total)

part_one()