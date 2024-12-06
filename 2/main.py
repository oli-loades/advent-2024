INPUT_FILENAME = "input.txt"

def get_input():
    with open(INPUT_FILENAME, "r", encoding="utf-8") as f:
        return [[int(vals) for vals in line.split()] for line in f ]

def row_safe(row):
    if row != sorted(row) and row != sorted(row, reverse=True):
        return False
    for x in range(len(row)-1):
        if not 1<=abs(row[x]-row[x+1])<=3:
            return False
    return True

def matrix_safe_count(func):
    safe = [func(row) for row in intput_matrix]
    return safe.count(True)

def safe_with_removal(row):
    if not row_safe(row):
        for x in range(len(row)):
            new_list = row[:x] + row[x+1:]
            if row_safe(new_list):
                return True
        return False
    return True

intput_matrix = get_input()
part_one = matrix_safe_count(row_safe)
print("part one: ",part_one)
part_two = matrix_safe_count(safe_with_removal)
print("part two: ", part_two)
