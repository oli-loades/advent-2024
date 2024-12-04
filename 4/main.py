INPUT_FILENAME = "input.txt"

def validate_xmas(xmas):
    return xmas == "XMAS" or xmas[::-1] == "XMAS"

def part_one(grid):
    found = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            char = grid[row][col] 
            if char == 'X':

                check_north = row - 3 >= 0
                check_east = col + 3 < len(grid[row])
                check_south = row + 3 < len(grid)
                check_west = col - 3 >= 0

                if check_north and validate_xmas("".join(grid[i][col] for i in range(row, row-4, -1))):
                    found.append((row,col, "N"))
                if (check_north and check_east) and validate_xmas("".join(grid[row-i][col+i] for i in range(4))):
                    found.append((row,col, "NE"))
                if check_east and validate_xmas("".join(grid[row][i]  for i in range(col, col+4))):
                    found.append((row,col, "E"))
                if (check_south and check_east) and validate_xmas("".join(grid[row+i][col+i] for i in range(4))):
                    found.append((row,col, "SE"))
                if check_south and validate_xmas("".join(grid[i][col] for i in range(row, row+4))):
                    found.append((row,col, "S"))
                if (check_south and check_west) and validate_xmas("".join(grid[row+i][col-i] for i in range(4))):
                    found.append((row,col, "SW"))
                if check_west and validate_xmas("".join(grid[row][i] for i in range(col, col-4, -1))):
                    found.append((row,col, "W"))
                if (check_north and check_west) and validate_xmas("".join(grid[row-i][col-i] for i in range(4))):
                    found.append((row,col, "NW"))
    print(len(found))

f = open(INPUT_FILENAME, "r")
grid = [[c for c in line if c.isalpha()] for line in f]
part_one(grid)




