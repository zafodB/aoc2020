# Day 11
# File contains top-down view of seating area where L is an empty seat, # is an occupied seat, and . is the floor.
# a) Each L or # has eight possible neighbours. If an L has 0 neighbours, it becomes a # and
# if an # has 4 or more neighbours it becomes an L. Find the number of # in the area after the area stops changing.
# b) Each L or # can "see" 8 possible neighbours. If an L has 0 neighbours, it becomes a # and
# if an # has 5 or more neighbours it becomes an L. Find the same.
 
import copy
 
f = open("10.1.input.txt")
content = f.read().split("\n")
grid = []
for line in content:
    row = []
    for char in line:
        row.append(char)
    grid.append(row)
 
running = True
iterations1 = 0
while running:
    iterations1 += 1
    newgrid = copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            neighbours = 0
            if i == 0 and j == 0:
                if grid[i+1][j] == "#":
                    neighbours += 1
                if grid[i][j+1] == "#":
                    neighbours += 1
                if grid[i+1][j+1] == "#":
                    neighbours += 1
            elif i == len(grid)-1 and j == len(grid[i])-1:
                if grid[i-1][j] == "#":
                    neighbours += 1
                if grid[i][j-1] == "#":
                    neighbours += 1
                if grid[i-1][j-1] == "#":
                    neighbours += 1
            elif i == 0 and j == len(grid[i])-1:
                if grid[i+1][j] == "#":
                    neighbours += 1
                if grid[i][j-1] == "#":
                    neighbours += 1
                if grid[i+1][j-1] == "#":
                    neighbours += 1
            elif i == len(grid)-1 and j == 0:
                if grid[i-1][j] == "#":
                    neighbours += 1
                if grid[i-1][j+1] == "#":
                    neighbours += 1
                if grid[i][j+1] == "#":
                    neighbours += 1
            elif i == 0 and 0 < j < len(grid[i])-1:
                if grid[i][j+1] == "#":
                    neighbours += 1
                if grid[i][j-1] == "#":
                    neighbours += 1
                if grid[i+1][j] == "#":
                    neighbours += 1
                if grid[i+1][j+1] == "#":
                    neighbours += 1
                if grid[i+1][j-1] == "#":
                    neighbours += 1
            elif i == len(grid)-1 and 0 < j < len(grid[i])-1:
                if grid[i][j+1] == "#":
                    neighbours += 1
                if grid[i][j-1] == "#":
                    neighbours += 1
                if grid[i-1][j] == "#":
                    neighbours += 1
                if grid[i-1][j+1] == "#":
                    neighbours += 1
                if grid[i-1][j-1] == "#":
                    neighbours += 1
            elif j == 0 and i != 0 < i < len(grid)-1:
                if grid[i+1][j] == "#":
                    neighbours += 1
                if grid[i+1][j+1] == "#":
                    neighbours += 1
                if grid[i-1][j+1] == "#":
                    neighbours += 1
                if grid[i-1][j] == "#":
                    neighbours += 1
                if grid[i][j+1] == "#":
                    neighbours += 1
            elif j == len(grid[i])-1 and 0 < i < len(grid)-1:
                if grid[i+1][j] == "#":
                    neighbours += 1
                if grid[i+1][j-1] == "#":
                    neighbours += 1
                if grid[i-1][j-1] == "#":
                    neighbours += 1
                if grid[i-1][j] == "#":
                    neighbours += 1
                if grid[i][j-1] == "#":
                    neighbours += 1
            elif 0 < i < len(grid)-1 and 0 < j < len(grid[i])-1:
                if grid[i][j+1] == "#":
                    neighbours += 1
                if grid[i][j-1] == "#":
                    neighbours += 1
                if grid[i+1][j] == "#":
                    neighbours += 1
                if grid[i-1][j] == "#":
                    neighbours += 1
                if grid[i+1][j+1] == "#":
                    neighbours += 1
                if grid[i+1][j-1] == "#":
                    neighbours += 1
                if grid[i-1][j+1] == "#":
                    neighbours += 1
                if grid[i-1][j-1] == "#":
                    neighbours += 1
            if grid[i][j] == "L" and neighbours == 0:
                newgrid[i][j] = "#"
            elif grid[i][j] == "#" and neighbours > 3:
                newgrid[i][j] = "L"
    if grid == newgrid:
        grid = copy.deepcopy(newgrid)
        running = False
    grid = copy.deepcopy(newgrid)
 
occ1 = 0
for row in grid:
    for item in row:
        if item == "#":
            occ1 += 1
 
grid = []
for line in content:
    row = []
    for char in line:
        row.append(char)
    grid.append(row)
 
iterations2 = 0
running = True
while running:
    iterations2 += 1
    newgrid = copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != ".":
                visiocc = 0
                # north
                checki = i
                checkj = j
                while checki-1 >= 0:
                    checki -= 1
                    if grid[checki][checkj] == "L":
                        break
                    if grid[checki][checkj] == "#":
                        visiocc += 1
                        break
                checki = i
                checkj = j
                # south
                while checki+1 <= len(grid)-1:
                    checki += 1
                    if grid[checki][checkj] == "L":
                        break
                    if grid[checki][checkj] == "#":
                        visiocc += 1
                        break
                # east
                checki = i
                checkj = j
                while checkj+1 <= len(grid[i])-1:
                    checkj += 1
                    if grid[checki][checkj] == "L":
                        break
                    if grid[checki][checkj] == "#":
                        visiocc += 1
                        break
                # west
                checki = i
                checkj = j
                while checkj-1 >= 0:
                    checkj -= 1
                    if grid[checki][checkj] == "L":
                        break
                    if grid[checki][checkj] == "#":
                        visiocc += 1
                        break
                # northeast
                checki = i
                checkj = j
                while checki-1 >= 0 and checkj+1 <= len(grid[i])-1:
                    checki -= 1
                    checkj += 1
                    if grid[checki][checkj] == "L":
                        break
                    if grid[checki][checkj] == "#":
                        visiocc += 1
                        break
                # northwest
                checki = i
                checkj = j
                while checki-1 >= 0 and checkj-1 >= 0:
                    checki -= 1
                    checkj -= 1
                    if grid[checki][checkj] == "L":
                        break
                    if grid[checki][checkj] == "#":
                        visiocc += 1
                        break
                # southeast
                checki = i
                checkj = j
                while checki+1 <= len(grid)-1 and checkj+1 <= len(grid[i])-1:
                    checki += 1
                    checkj += 1
                    if grid[checki][checkj] == "L":
                        break
                    if grid[checki][checkj] == "#":
                        visiocc += 1
                        break
                # southwest
                checki = i
                checkj = j
                while checki+1 <= len(grid)-1 and checkj-1 >= 0:
                    checki += 1
                    checkj -= 1
                    if grid[checki][checkj] == "L":
                        break
                    if grid[checki][checkj] == "#":
                        visiocc += 1
                        break
                if grid[i][j] == "#" and visiocc >= 5:
                    newgrid[i][j] = "L"
                if grid[i][j] == "L" and visiocc == 0:
                    newgrid[i][j] = "#"
    if grid == newgrid:
        grid = copy.deepcopy(newgrid)
        running = False
    grid = copy.deepcopy(newgrid)
 
occ2 = 0
for row in grid:
    for item in row:
        if item == "#":
            occ2 += 1
 
print(f"The number of occupied seats in the area when equilibrium is reached following ruleset #1 in {iterations1}"
      f" iterations is {occ1}.")
print(f"The number of occupied seats in the area when equilibrium is reached following ruleset #2 in {iterations2}"
      f" iterations is {occ2}.")