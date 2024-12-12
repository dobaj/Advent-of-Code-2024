cardinals = (-1, 0), (1, 0), (0, -1), (0, 1)

def inRange(x, y, farm):
    if y >= 0 and y < len(farm):
        return x >= 0 and x < len(farm[y])
    return False

def addDict(dict, key, val):
    if key in dict:
        dict[key] += val
    else:
        dict[key] = val

def fillGarden(farm):
    visited = [] 
    for y in range(len(farm)):
        visited.append([0] * len(farm[0]))
    area = {}
    perimeter = {}
    gardenIndex = 0

    toVisit = [(0,0)]

    while len(toVisit):
        newVisit = []

        for x,y in toVisit: 
            if not visited[y][x]:
                value = farm[y][x]
                visited[y][x] = 1
                adjacent = 0

                for cX, cY in cardinals:
                    newX, newY = x+cX, y+cY
                    if inRange(newX, newY, farm):
                        if farm[newY][newX] == value:
                            # No fence here
                            adjacent += 1
                            if not visited[newY][newX]:
                                # Adds patches of matching value
                                newVisit.append((newX,newY))

                addDict(area,gardenIndex,1)
                addDict(perimeter,gardenIndex,4-adjacent)
        
        if len(newVisit) == 0:
            # Find the next garden to investigate
            for y in range(len(visited)):
                for x in range(len(visited[y])):
                    if not visited[y][x]:
                        gardenIndex+=1
                        newVisit.append((x,y))
                        break
                if len(newVisit) > 0:
                    break
        
        toVisit = newVisit

    return area, perimeter

def findSide(sides, gardenIndex, x, y, direction):
    vertical = direction[1] == 0

    # Get major and minor axes of side
    coord = x
    othercoord = y
    if vertical:
        coord = y
        othercoord = x

    if gardenIndex not in sides:
        sides[gardenIndex] = []
    else:
        for i, side in enumerate(sides[gardenIndex]):
            # Check if a matching side already exists
            if side[0] == direction and side[1] == othercoord:
                if coord == side[2] - 1:
                    sides[gardenIndex][i] = side[0], side[1], side[2]-1, side[3]
                    return
                elif coord == side[3] + 1:
                    sides[gardenIndex][i] = side[0], side[1], side[2], side[3]+1
                    return

    # Store as direction, othercoord, min, max
    sides[gardenIndex].append((direction, othercoord, coord, coord))


def fillGardenSides(farm):
    visited = [] 
    for y in range(len(farm)):
        visited.append([0] * len(farm[0]))
    area = {}
    sides = {}
    gardenIndex = 0

    toVisit = [(0,0)]

    while len(toVisit):
        newVisit = []

        for x,y in toVisit: 
            if not visited[y][x]:
                value = farm[y][x]
                visited[y][x] = 1

                for cX, cY in cardinals:
                    newX, newY = x+cX, y+cY
                    if inRange(newX, newY, farm) and farm[newY][newX] == value:
                        if not visited[newY][newX]:
                            # Adds patches of matching value
                            newVisit.append((newX,newY))
                    else:
                        # see if theres a side for this, if not add it
                        findSide(sides,gardenIndex,newX,newY,(cX,cY))

                addDict(area,gardenIndex,1)
        
        if len(newVisit) == 0:
            # Find the next garden to investigate
            for y in range(len(visited)):
                for x in range(len(visited[y])):
                    if not visited[y][x]:
                        gardenIndex+=1
                        newVisit.append((x,y))
                        break
                if len(newVisit) > 0:
                    break
        
        toVisit = newVisit

    return area, sides

def part1() -> None:
    farm = []

    with open("Day 12/input.txt") as f:
        for line in f:
            farm.append(line.strip())
    
    scores = 0

    area, perimeter = fillGarden(farm)

    for key in area.keys():
        # Summate
        scores+=area[key]*perimeter[key]
    
    print("Part 1:", scores)

def part2() -> None:
    farm = []

    with open("Day 12/input.txt") as f:
        for line in f:
            farm.append(line.strip())
    
    scores = 0

    area, sides = fillGardenSides(farm)

    for key in area.keys():
        # Summate
        scores+=area[key]*len(sides[key])
    
    print("Part 2:", scores)

part1()
part2()