INPUT_FILENAME = "input.txt"

def get_input():
    f = open(INPUT_FILENAME, "r")
    return [[int(vals) for vals in line.split()] for line in f ]

def row_safe(list):
    # check that all values are increasing or decreasing
    if list != sorted(list) and list != sorted(list, reverse=True):
        return False
    
    for x in range(len(list)-1):
        if not 1<=abs(list[x]-list[x+1])<=3:
            return False
    return True

def matrix_safe(matrix):
    return [row_safe(row) for row in matrix]

intput_matrix = get_input()
safe = matrix_safe(intput_matrix)
safe_count = safe.count(True)
print(safe_count)
