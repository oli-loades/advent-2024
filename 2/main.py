INPUT_FILENAME = "input.txt"

def get_input():
    f = open(INPUT_FILENAME, "r")
    return [[int(vals) for vals in line.split()] for line in f ]

def row_safe(list):
    if list != sorted(list) and list != sorted(list, reverse=True):
        return False
    
    for x in range(len(list)-1):
        if not 1<=abs(list[x]-list[x+1])<=3:
            return False
    return True

def matrix_safe_count(matrix, func):
    safe = [func(row) for row in matrix]
    return safe.count(True)

def safe_with_removal(list):
    if (row_safe(list) == False):
        for x in range(len(list)):
            new_list = list[:x] + list[x+1:]
            if row_safe(new_list) == True:
                return True
        return False
    else:
        return True

intput_matrix = get_input()
part_one = matrix_safe_count(intput_matrix, row_safe)
print("part one: ",part_one)
part_two = matrix_safe_count(intput_matrix, safe_with_removal)
print("part two: ", part_two)
