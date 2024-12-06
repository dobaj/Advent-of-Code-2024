import sys

# Im sorry
sys.setrecursionlimit(10000)

def turn90(direction):
    match direction:
        case (0, -1): # Up
            return (1, 0) # Right
        case (1, 0): # Right
            return (0, 1) # Down
        case (0, 1): # Down
            return (-1, 0) # Left
        case (-1, 0): # Left
            return (0, -1) # Up


def movePart1(obstacles: set, distinctPositions: set, guardPos: tuple, direction: tuple, maxX: int, maxY: int):
        (x,y) = guardPos[0]+direction[0], guardPos[1]+direction[1]

        if not inRange(guardPos[0], guardPos[1], maxX, maxY):
            return False
        
        distinctPositions.add(guardPos)
        
        newDirection = turn90(direction)

        if (x,y) in obstacles:

            return movePart1(obstacles, distinctPositions, guardPos, newDirection, maxX, maxY)
        
        else:
            return movePart1(obstacles, distinctPositions, (x, y), direction, maxX, maxY)

def inRange(x, y, maxX, maxY):
    return x >= 0 and x < maxX and y >= 0 and y < maxY



def part1() -> None:
    obstacles = set()
    distinctPositions = set()
    direction = (0, -1) # x, y
    guardPos = (0, 0)
    maxX, maxY = 0, 0

    with open("Day 06/input.txt") as f:
        for y, line in enumerate(f):
            maxY += 1
            maxX = max(maxX, len(line.strip()))
            for x, item in enumerate(line.strip()):
                if item == "^": # Guard always faces up
                    guardPos = (x, y)
                elif item == "#": 
                    obstacles.add((x, y))

    # Go through route
    movePart1(obstacles, distinctPositions, guardPos, direction, maxX, maxY)

    print("Part 1:", len(distinctPositions))

def movePart2(obstacles: set, obstaclesWDir: set, guardPos: tuple, direction: tuple, maxX: int, maxY: int):
    (x,y) = guardPos[0]+direction[0], guardPos[1]+direction[1]

    if not inRange(guardPos[0], guardPos[1], maxX, maxY):
        return False

    if (x,y, direction) in obstaclesWDir:
        # LOOP TIME
        return True
    
    newDirection = turn90(direction)

    if (x,y) in obstacles:
        obstaclesWDir.add((x,y, direction))

        return movePart2(obstacles, obstaclesWDir, guardPos, newDirection, maxX, maxY)
    
    else:
        return movePart2(obstacles, obstaclesWDir, (x, y), direction, maxX, maxY)


def part2() -> None:
    obstacles = set()
    obstaclesWDir = set()
    distinctPositions = set()
    direction = (0, -1) # x, y
    guardPos = (0, 0)
    loops = 0
    
    maxX, maxY = 0, 0

    with open("Day 06/input.txt") as f:
        for y, line in enumerate(f):
            maxY += 1
            maxX = max(maxX, len(line.strip()))
            for x, item in enumerate(line.strip()):
                if item == "^": # Guard always faces up
                    guardPos = (x, y)
                elif item == "#": 
                    obstacles.add((x,y))

    movePart1(obstacles, distinctPositions, guardPos, direction, maxX, maxY)

    # Go through route, get rid of initial position (we can't put an obstacle there)
    distinctPositions.discard(guardPos)

    for newObstacle in distinctPositions:
        newObstacles = obstacles.copy()
        newObstacles.add(newObstacle)

        obstaclesWDir = set()

        if movePart2(newObstacles, obstaclesWDir, guardPos, direction, maxX, maxY):
            loops+=1
    
    print("Part 2:", loops)

part1()
part2()