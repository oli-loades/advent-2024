INPUT_FILENAME = "input.txt"

def get_input():
    with open(INPUT_FILENAME, "r", encoding="utf-8") as f:
        return [list(line.strip()) for line in f]

def find_start_pos():
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if col == '^':
                return (row_index, col_index)

def part_one():
    direction = 1
    stop = False
    row, col = start_pos
    visited = set()
    while not stop:
        if direction == 1:
            if grid[row-1][col] == '#':
                direction = 2
            else:
                visited.add((row,col))
                row -= 1
        elif direction == 2:
            if grid[row][col+1] == '#':
                direction = 3
            else:
                visited.add((row,col))
                col += 1
        elif direction == 3:
            if grid[row+1][col] == '#':
                direction = 4
            else:
                visited.add((row,col))
                row += 1
        else:
            if grid[row][col-1] == '#':
                direction = 1
            else:
                visited.add((row,col))
                col -= 1
        if row >= len(grid) or row < 0 or col >= len(grid[row]) or col < 0:
            stop = True
    print("part one:", len(visited))

grid = get_input()
start_pos = find_start_pos()
part_one()
