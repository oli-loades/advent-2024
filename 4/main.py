INPUT_FILENAME = "input.txt"

def validate_xmas(xmas):
    return xmas == "XMAS" or xmas[::-1] == "XMAS"

def part_one():
    total = 0
    for row_index, row in enumerate(grid):
        for col_idenx, char in enumerate(row):
            if char == 'X':

                check_north = row_index - 3 >= 0
                check_east = col_idenx + 3 < len(row)
                check_south = row_index + 3 < len(grid)
                check_west = col_idenx - 3 >= 0

                if check_north and validate_xmas("".join(grid[i][col_idenx] for i in range(row_index, row_index-4, -1))):
                    total += 1
                if (check_north and check_east) and validate_xmas("".join(grid[row_index-i][col_idenx+i] for i in range(4))):
                    total += 1
                if check_east and validate_xmas("".join(grid[row_index][i]  for i in range(col_idenx, col_idenx+4))):
                    total += 1
                if (check_south and check_east) and validate_xmas("".join(grid[row_index+i][col_idenx+i] for i in range(4))):
                    total += 1
                if check_south and validate_xmas("".join(grid[i][col_idenx] for i in range(row_index, row_index+4))):
                    total += 1
                if (check_south and check_west) and validate_xmas("".join(grid[row_index+i][col_idenx-i] for i in range(4))):
                    total += 1
                if check_west and validate_xmas("".join(grid[row_index][i] for i in range(col_idenx, col_idenx-4, -1))):
                    total += 1
                if (check_north and check_west) and validate_xmas("".join(grid[row_index-i][col_idenx-i] for i in range(4))):
                    total += 1
    print(total)

def part_two():
    options = ["MMSS", "SMMS", "SSMM", "MSSM"]
    total = 0
    for row in range(1, len(grid)-1):
        for col in range(1, len(grid[row])-1):
            char = grid[row][col] 
            if char == 'A' and options.count(grid[row-1][col-1] + grid[row-1][col+1] + grid[row+1][col+1] + grid[row+1][col-1]) == 1:
                total += 1
    print(total)

with open(INPUT_FILENAME, "r", encoding="utf-8") as f:
    grid = [[c for c in line if c.isalpha()] for line in f]
    part_one()
    part_two()
