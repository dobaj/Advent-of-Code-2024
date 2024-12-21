from heapq import *

directions = [(1,0), (0,1), (-1,0), (0,-1)]

def inRange(x, y, grid):
    if y >= 0 and y < len(grid):
        return x >= 0 and x < len(grid[y])
    return False

def noCheat(grid, start, end):
    # Run a preliminary search to see what to compare cheats to
    visited = set()

    toVisit = [start]
    heapify(toVisit)

    while len(toVisit) > 0:
        steps, x, y = heappop(toVisit)

        if (x, y) == end:
            return steps

        if (x,y) in visited:
            continue

        for (dx, dy) in directions:
            newX, newY = x+dx, y+dy

            if (newX, newY) not in visited:
                if inRange(newX,newY,grid):
                    if grid[newY][newX] != "#":
                        heappush(toVisit,(steps+1, newX, newY))

        visited.add((x,y))

    return -1

def generateLenMap(grid, end):
    # Fill a new grid with distance from the end point

    newMap = []
    for y in range(len(grid)):
        row = []
        for x in range(len(grid[y])):
            row += [-1]
        newMap.append(row)

    visited = set()

    toVisit = [(0,end[0],end[1])]
    heapify(toVisit)

    while len(toVisit) > 0:
        steps,x,y = heappop(toVisit)

        if (x,y) in visited:
            continue

        for (dx, dy) in directions:
            newX, newY = x+dx, y+dy

            if (newX, newY) not in visited:
                if inRange(newX,newY,grid):
                    if grid[newY][newX] != "#":
                        heappush(toVisit,(steps+1, newX,newY))
        
        newMap[y][x] = steps

        visited.add((x,y))
    
    return newMap

def getAllCheatEndings(circleList, grid, afterCheatMap, cheatStart, noCheats, prevSteps, threshold):
    sum=0
    for steps, newX, newY in circleList:
        newX,newY = cheatStart[0]+newX, cheatStart[1]+newY

        if inRange(newX,newY,grid) and grid[newY][newX] != "#":
            
            time = afterCheatMap[newY][newX]+steps+prevSteps
            if time <= noCheats - threshold:
                sum+=1

    return sum

def circle(cheats):
    visited = set()

    allVisit = set()

    toVisit = [(0,0,0)]
    heapify(toVisit)

    while len(toVisit) > 0:
        steps, x, y = heappop(toVisit)

        if steps > cheats:
            continue

        if (x,y) in visited:
            continue

        for (dx, dy) in directions:
            newX, newY = x+dx, y+dy

            if (newX, newY) not in visited:
                heappush(toVisit,(steps+1,newX,newY))
        
        visited.add((x,y))
        allVisit.add((steps,x,y))

    return list(allVisit)

def escape(grid, start, end, cheats):
    visited = set()
    afterCheatMap = generateLenMap(grid,end) 
    noCheats = afterCheatMap[start[2]][start[1]]
    circleList = circle(cheats)
    cheated = 0


    toVisit = [start]
    heapify(toVisit)


    while len(toVisit) > 0:
        steps, x, y = heappop(toVisit)

        if (x,y) in visited:
            continue

        for (dx, dy) in directions:
            newX, newY = x+dx, y+dy

            if (newX, newY) not in visited:
                if inRange(newX,newY,grid):
                    if grid[newY][newX] != "#":
                        heappush(toVisit,(steps+1, newX, newY))
        
        # Can cheat whenever we are on a path
        cheated+=getAllCheatEndings(circleList,grid,afterCheatMap,(x,y),noCheats,steps,100)

        visited.add((x,y))
    
    return cheated

def part1() -> None:
    with open("Day 20/input.txt") as f:
        start, end = (0,0,0), (0,0)
        grid = []

        for y, line in enumerate(f):
            row = []
            for x, char in enumerate(line.strip()):
                if char == "S":
                    start = (0, x, y)
                    row += "."
                elif char == "E":
                    end = (x, y)
                    row += "."
                else:
                    row += char
            grid.append(row)
        
        print("Part 1:", escape(grid, start, end, 2))


def part2() -> None:
    with open("Day 20/input.txt") as f:
        start, end = (0,0,0), (0,0)
        grid = []

        for y, line in enumerate(f):
            row = []
            for x, char in enumerate(line.strip()):
                if char == "S":
                    start = (0, x, y)
                    row += "."
                elif char == "E":
                    end = (x, y)
                    row += "."
                else:
                    row += char
            grid.append(row)
        
        print("Part 2:", escape(grid, start, end, 20))

part1()
part2()