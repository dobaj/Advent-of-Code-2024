moveMap = {
    "<": (-1,0),
    "^": (0,-1),
    ">": (1, 0),
    "v": (0, 1)
}

def move(whMap, pos, direction):
    x, y = pos
    dx, dy = direction

    if whMap[y][x] == ".":
        return True, pos
    if whMap[y][x] == "#":
        return False, pos
    
    if move(whMap, (x+dx, y+dy), direction)[0] == True:
        whMap[y+dy][x+dx] = whMap[y][x]
        whMap[y][x] = "."
        return True, (x+dx, y+dy)
    
    return False, pos

def printMap(whMap):
    for row in whMap:
        rowStr = ""
        for char in row:
            rowStr+=char
        print(rowStr)

def part1() -> None:
    with open("Day 15/input.txt") as f:
        whMap = [] # Map of warehouse
        robot = (0, 0)
        y=0

        line = f.readline()
        while line != "\n":
            row = []
            for x, char in enumerate(line.strip()):
                row+=char
                if char == "@":
                    robot = (x, y)
            whMap.append(row)
            line, y = f.readline(), y+1
        
        line = f.readline()
        while line:
            for movement in line.strip():
                robot = move(whMap, robot, moveMap[movement])[1]
            line = f.readline()

        # Get GPS sum
        sum = 0
        for y, row in enumerate(whMap):
            for x, char in enumerate(row):
                if char == "O":
                    sum+=100*y+x

        print("Part 1:", sum)

def mapAt(whMap, pos):
    return whMap[pos[1]][pos[0]]

def checkMove(whMap, pos, direction):
    # Does not move, only checks if its safe
    x, y = pos
    dx, dy = direction
    char = whMap[y][x]

    if char == ".":
        return True
    if char == "#":
        return False
    
    if (char == "]" or char == "[") and dy != 0:
        # We now need to check twice
        if char == "]":
            nextOtherCoord = (x-1+dx, y+dy)
        else:
            nextOtherCoord = (x+1+dx, y+dy)

        return checkMove(whMap, (x+dx, y+dy), direction) and checkMove(whMap, nextOtherCoord, direction)

    return checkMove(whMap, (x+dx, y+dy), direction)

def move2(whMap, pos, direction):
    # Moves once it has been cleared to be safe
    x, y = pos
    dx, dy = direction
    char = whMap[y][x]

    if char == ".":
        return pos
    if char == "#":
        return pos
    
    # Always move
    move2(whMap, (x+dx, y+dy), direction)
    whMap[y+dy][x+dx] = char
    whMap[y][x] = "."

    if (char == "]" or char == "[") and dy != 0:
        if char == "]":
            otherCoord = (x-1, y)
            nextOtherCoord = (x-1+dx, y+dy)
        else:
            otherCoord = (x+1, y)
            nextOtherCoord = (x+1+dx, y+dy)

        move2(whMap, nextOtherCoord, direction)
        whMap[y+dy][nextOtherCoord[0]] = mapAt(whMap,otherCoord)
        whMap[y][nextOtherCoord[0]] = "."
    
    return (x+dx, y+dy)

def part2() -> None:
    with open("Day 15/input.txt") as f:
        whMap = [] # Map of warehouse
        robot = (0, 0)
        y=0

        line = f.readline()
        while line != "\n":
            row = []
            for x, char in enumerate(line.strip()):
                if char == "O":
                    row+="["+"]"
                elif char == "@":
                    row+=char+"."
                    robot = (x*2, y)
                else:
                    row+=[char]*2
            whMap.append(row)
            line, y = f.readline(), y+1

        line = f.readline()
        while line:
            for movement in line.strip():
                # Now we need to check if a move is safe
                safe = checkMove(whMap, robot, moveMap[movement])
                if safe:
                    robot = move2(whMap, robot, moveMap[movement])
            line = f.readline()

        # Get GPS sum
        sum = 0
        for y, row in enumerate(whMap):
            for x, char in enumerate(row):
                if char == "[":
                    sum+=100*y+x

        print("Part 2:", sum)

part1()
part2()