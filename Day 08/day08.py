def addAntenna(antennae, antenna, x, y):
    if antenna not in antennae:
        antennae[antenna] = [(x,y)]
    else:
        antennae[antenna].append((x,y))

def inRange(maxX, maxY, x, y):
    return x >= 0 and x < maxX and y >= 0 and y < maxY

def part1() -> None:
    antennae = {}
    antinodes = set()
    maxX, maxY = 0, 0

    with open("Day 08/input.txt") as f:
        for y, line in enumerate(f):
            maxY+=1
            maxX=max(maxX, len(line.strip()))

            for x, antenna in enumerate(line.strip()):
                if antenna.isalnum():
                    addAntenna(antennae, antenna, x, y)


    for antenna in antennae:
        for loc1 in antennae[antenna]:
            for loc2 in antennae[antenna]:
                # Find every pair. This could be optimized but it's fast enough
                if loc1 != loc2:
                    deltaX, deltaY = loc2[0]-loc1[0], loc2[1]-loc1[1]

                    # Follow the line between the two antennae
                    antinodeX, antinodeY = loc1[0]+2*deltaX, loc1[1]+2*deltaY
                    if inRange(maxX, maxY, antinodeX, antinodeY):
                        antinodes.add((antinodeX, antinodeY))
    print("Part 1:", len(antinodes))

def part2() -> None:
    antennae = {}
    antinodes = set()
    maxX, maxY = 0, 0

    with open("Day 08/input.txt") as f:
        for y, line in enumerate(f):
            maxY+=1
            maxX=max(maxX, len(line.strip()))
            
            for x, antenna in enumerate(line.strip()):
                if antenna.isalnum():
                    addAntenna(antennae, antenna, x, y)
        
        
    for antenna in antennae:
        for loc1 in antennae[antenna]:
            for loc2 in antennae[antenna]:
                # Find every pair. This could be optimized but it's fast enough
                if loc1 != loc2:
                    deltaX, deltaY = loc2[0]-loc1[0], loc2[1]-loc1[1]
                    
                    # Follow the line between the two antennae
                    antinodeX, antinodeY = loc1[0]+deltaX, loc1[1]+deltaY
                    while inRange(maxX, maxY, antinodeX, antinodeY):
                        antinodes.add((antinodeX, antinodeY))
                        antinodeX, antinodeY = antinodeX+deltaX, antinodeY+deltaY
    print("Part 2:", len(antinodes))

part1()
part2()