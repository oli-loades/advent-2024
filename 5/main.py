from collections import defaultdict

INPUT_FILENAME = "input.txt"

def get_input():
    f = open(INPUT_FILENAME, "r", encoding="utf-8")

    rules, sections = defaultdict(set), []
    for line in f:
        if "|" in line:
            a, b = line.split("|")
            a, b = int(a), int(b)
            rules[b].add(a)
        elif "," in line:
            section = [int(vals) for vals in line.split(",")]
            sections.append(section)
    return rules, sections

def validate_section(rules, section):
    for i,x in enumerate(section):
        for j,y in enumerate(section):
            if i<j and y in rules[x]:
                return False
    return True

def part_one(rules, sections):
    total = 0
    for section in sections:
        valid = validate_section(rules, section)
        if valid: total += section[len(section)//2]
    print(total)

rules, sections = get_input()
part_one(rules, sections)
