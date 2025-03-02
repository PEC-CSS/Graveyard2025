import copy

def validInput(grid, n):
    for i in range(0, len(grid)):
        if(len(grid[i]) != int(n)):
            print(n)
            print(grid[i])
            print("length", len(grid[i]))
            return False
        for j in range(0, int(n)):
            if(grid[i][j] != "1" and grid[i][j] != "0" and grid[i][j] != "2"):
                print("element", grid[i][j])
                return False
    return True

def isCorrupt(grid):
    for row in range(0, len(grid)):
        for column in range(0, len(grid[row])):
            if (grid[row][column] == "1"):
                return True
    return False

def canCorrupt(grid):
    rowCheck = False
    columnCheck = False
    for row in range(0, len(grid)):
        for column in range(0, len(grid[row])):
            if (grid[row][column] == "1"):
                if (column == 0):
                    if (grid[row][column + 1] == "0"):
                        rowCheck = True
                elif (column == len(grid[row]) - 1):
                    if (grid[row][column - 1] == "0"):
                        rowCheck = True
                else:
                    if (grid[row][column - 1] == "0" and grid[row][column + 1] == "0"):
                        rowCheck = True

                if (row == 0):
                    if (grid[row + 1][column] == "0"):
                        columnCheck = True
                elif (row == len(grid) - 1):
                    if (grid[row - 1][column] == "0"):
                        columnCheck = True
                else:
                    if (grid[row - 1][column] == "0" and grid[row + 1][column] == "0"):
                        columnCheck = True

    return not(rowCheck and columnCheck)

def spreadCorrupt(grid):
    newgrid = copy.deepcopy(grid)
    for row in range(0, len(grid)):
        for column in range(0, len(grid[row])):
            if (grid[row][column] == "2"):
                if (column == 0):
                    newgrid[row][column + 1] = "2"
                elif (column == len(grid[row]) - 1):
                    newgrid[row][column - 1] = "2"
                else:
                    newgrid[row][column - 1] = "2"
                    newgrid[row][column + 1] = "2"

                if (row == 0):
                    newgrid[row + 1][column] = "2"
                elif (row == len(grid) - 1):
                    newgrid[row - 1][column] = "2"
                else:
                    newgrid[row - 1][column] = "2"
                    newgrid[row + 1][column] = "2"
    return newgrid

gridDimensions = input().split()
grid = []
for i in range(0, int(gridDimensions[0])):
    grid.insert(0, input().split())
grid.reverse()

if(validInput(grid, gridDimensions[1])):
    if(isCorrupt(grid)):
        if(canCorrupt(grid)):
            minutes = 0
            while(isCorrupt(grid)):
                grid = spreadCorrupt(grid)
                minutes += 1  
            print(minutes)
        else:
            print("-1")
    else:
        print("0")
else:
    print("Invalid Input")
