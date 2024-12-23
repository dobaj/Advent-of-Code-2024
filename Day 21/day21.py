from heapq import *

numeric = ["789",
           "456",
           "123",
           " 0A"]
directional = [" ^A", 
               "<v>"]

directions = [(1,0,">"), (0,1,"v"), (-1,0,"<"), (0,-1,"^")]

buttonMemo = {}

def inRange(x, y, grid):
    if y >= 0 and y < len(grid):
        return x >= 0 and x < len(grid[y]) and grid[y][x] != " "
    return False

def findA(arr: list[str]):
    for y,s in enumerate(arr):
        try:
            return (s.index("A"), y)
        except ValueError:
            pass
    return (-1,-1)

def pathFind(keyPad, start, endChar):
    toVisit = [(0, start[0],start[1], "")]
    heapify(toVisit)

    shortest = []
    endPos = (0,0)
    shortVal = -1

    while len(toVisit) > 0:
        score, x, y, path = heappop(toVisit)

        if shortVal != -1 and score > shortVal:
            break

        if keyPad[y][x] == endChar:
            shortest.append((path+"A"))
            endPos = (x,y)
            shortVal = score
        
        for dx, dy, char in directions:
            newX, newY = x+dx, y+dy

            if inRange(newX, newY, keyPad):
                heappush(toVisit,(score+1, newX, newY, path+char))

    return endPos, shortest

def getPathLen(keyMap, endResult, depth, i = 0):
    if i == depth:
        # Get smallest path
        return min(map(len,endResult))
    
    allPathLengths = []
    
    for endPath in endResult:
        # For all variations

        paths = []
        pathLen = 0

        if (endPath, depth-i) in buttonMemo:
            # Memoize
            pathLen = buttonMemo[(endPath, depth-i)]
        else:
            position = findA(keyMap)

            for char in endPath:
                # Find how to move robot to correct key
                position, newPaths = pathFind(keyMap, position, char)    
                paths.append(newPaths)   

            for j, p in enumerate(paths):
                # Now get shortest path to this button
                paths[j] = getPathLen(directional, p, depth, i+1)
            
            pathLen = sum(paths)

            buttonMemo[(endPath, depth-i)] = pathLen

        allPathLengths.append(pathLen)
    
    return min(allPathLengths)


def part1() -> None:
    with open("Day 21/input.txt") as f:
        sum=0
        for line in f:
            line = line.strip()

            val = getPathLen(numeric, [line], 3, 0)

            # print(line, val)
            sum+=val*int(line[:-1])
            

        print("Part 1:", sum)

def part2() -> None:
    with open("Day 21/input.txt") as f:
        sum=0
        for line in f:
            line = line.strip()
                    
            val = getPathLen(numeric, [line], 26, 0)

            # print(line, val)
            sum+=val*int(line[:-1])
            

        print("Part 2:", sum)

part1()
part2()