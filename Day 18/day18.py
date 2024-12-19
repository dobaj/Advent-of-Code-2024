from heapq import *

GRID_SIZE = 71
directions = [(1,0), (0,1), (-1,0), (0,-1)]

def inRange(x, y):
    if y >= 0 and y < GRID_SIZE:
        return x >= 0 and x < GRID_SIZE
    return False

def escape(grid, start = (0,0,0,[]), end = (GRID_SIZE-1,GRID_SIZE-1)):
    visited = set()

    toVisit = [start]
    heapify(toVisit)

    while len(toVisit) > 0:
        steps, x, y, path = heappop(toVisit)

        if (x,y) == end:
            return steps

        if (x,y) in visited:
            continue

        for (dx, dy) in directions:
            newX, newY = x+dx, y+dy

            if (newX, newY) not in visited:
                if inRange(newX,newY) and grid[newY][newX] != "#":
                    heappush(toVisit,(steps+1, newX, newY, path+[(x,y)]))
        
        visited.add((x,y))

    return -1

def printGrid(grid, path=[]):
    for y, row in enumerate(grid):
        line = ""
        for x, col in enumerate(row):
            if (x,y) in path:
                line+="O"
            elif col:
                line+=col
            else:
                line+=" "
        print(line)

def part1() -> None:
    with open("Day 18/input.txt") as f:
        grid = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

        i = 0
        line = f.readline()
        while line and i < 1024:
            x, y = map(lambda x: int(x), line.strip().split(","))
            grid[y][x] = "#"
            i, line = i+1, f.readline()
        
        print("Part 1:", escape(grid))

def generateGridAfterTime(i, parentGrid):
    # return grid as of a certain time
    grid = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for y, row in enumerate(parentGrid):
        for x, col in enumerate(row):
            if col:
                time, val = col
                if time < i:
                    grid[y][x] = val
    return grid

def getByte(i, parentGrid):
    for y, row in enumerate(parentGrid):
        for x, col in enumerate(row):
            if col:
                time, _ = col
                if time == i:
                    return f"{x},{y}"

def part2() -> None:
    with open("Day 18/input.txt") as f:
        grid = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        i = 0
        line = f.readline()
        while line:
            x, y = map(lambda x: int(x), line.strip().split(","))
            if not grid[y][x]:
                grid[y][x] = (i,"#")
            i, line = i+1, f.readline()

        # Binary search
        sm, lg = 0, i
        while sm <= lg:
            mid = (sm+lg) // 2

            result = escape(generateGridAfterTime(mid,grid))

            if result == -1: # Too high
                lg = mid-1
            else:
                sm = mid+1
            
        print("Part 2:", getByte(sm-1,grid)) # Get byte right before it fails

part1()
part2()