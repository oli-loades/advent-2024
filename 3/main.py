import re

INPUT_FILENAME = "input.txt"

def part_one():
    with open(INPUT_FILENAME, "r", encoding="utf-8") as f:
        pattern = r"mul\((\d+),(\d+)\)"
        total = 0
        for line in f:
            for match in re.findall(pattern, line):
                total += int(match[0]) * int(match[1])
        print("part one: ", total)

def part_two():
    with open(INPUT_FILENAME, "r", encoding="utf-8") as f:
        pattern = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"
        total = 0
        disabled = False
        for line in f:
            for match in re.findall(pattern, line):
                if not disabled and match[0] != "" and match[1] != "":
                    total += int(match[0]) * int(match[1])
                if match[2] != "":
                    disabled = False
                if match[3] != "":
                    disabled = True
        print("part two: ", total)

part_one()
part_two()
