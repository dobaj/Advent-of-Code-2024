import re

maxes = [101,103]

def extractPair(str):
    # Get int pair for str rep
    pair = tuple(map(lambda x: int(x), str.split(',')))
    return pair

def move(pos,vel,time):
    # Because they can wrap around and they move in straight lines, this is pretty easy
    nextPos = []
    for i, axis in enumerate(pos):
        nextPos.append((axis+vel[i]*time) % maxes[i])
    return tuple(nextPos)

def quadrant(pos):
    middles = [(x-1)/2 for x in maxes]

    x = -1
    y = -1

    if pos[1] > middles[1]:
        y = 2
    elif pos[1] < middles[1]:
        y = 0
    
    if pos[0] < middles[0]:
        x = 0
    elif pos[0] > middles[0]:
        x = 1
    
    if x >= 0 and y >= 0:
        return x+y 
    
    return -1
        

def part1() -> None:
    robots = [] # Tuple of pos, velocity
    quadCount = [0] * 4

    with open("Day 14/input.txt") as f:
        for line in f:
            robot = tuple(map(extractPair, re.findall("-?[0-9]*,-?[0-9]*",line)))
            robots.append(robot)
    
    for robot in robots:
        nextPos = move(robot[0],robot[1],100)
        quad = quadrant(nextPos)
        if quad >= 0:
            quadCount[quad] += 1
    
    prod = 1
    for quad in quadCount:
        prod*=quad
    print("Part 1:", prod)

def printMap(robotMap, i):
    print(i,"-"*150)
    for y in range(maxes[1]):
        line=""
        for x in range(maxes[0]):
            if (x,y) in robotMap:
                line+="X"
            else:
                line+=" "
        print(line)

def maxPerLine(robotMap):
    # Maximum robots on one row
    lineCount = 0
    for y in range(maxes[1]):
        temp = 0
        for x in range(maxes[0]):
            if (x,y) in robotMap:
                temp+=1
        lineCount = max(lineCount, temp)
    return lineCount

def part2() -> None:
    # Make a set of locations
    robotMap = set()
    robots = [] # Tuple of pos, velocity

    with open("Day 14/input.txt") as f:
        for line in f:
            robot = tuple(map(extractPair, re.findall("-?[0-9]*,-?[0-9]*",line)))
            robots.append(robot)
    
    i = 0
    initialRobots = None
    maxLine = (0,0,0)
    with open("Day 14/output.txt", "w") as f:
        while True:
            nextRobots=[]
            for robot in robots:
                nextPos = move(robot[0],robot[1],i)
                robotMap.add(nextPos)
                nextRobots.append(nextPos)

            # Check if robots loop
            if initialRobots == None:
                initialRobots = tuple(nextRobots)
            else:
                if tuple(nextRobots) == initialRobots:
                    # We have looped over everything
                    break
            
            # Get map with a picture frame ( Prob most Xs in a row)
            maxinLine = maxPerLine(robotMap)
            if maxinLine > maxLine[1]:
                maxLine = (i, maxinLine, robotMap)
            robotMap = set()
            i+=1
    print("Part 2:", maxLine[0])
    printMap(maxLine[2],maxLine[0])

part1()
part2()