cardinals = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def inRange(x, y, rows):
    if y >= 0 and y < len(rows):
        return x >= 0 and x < len(rows[y])
    return False

def move(x, y, rows, path = []):
    val = rows[y][x]
    reachable = set() # different paths
    rating = set()

    if val == 9:
        reachable.add((x,y))
        path.append((x,y)) # Different nines can have the same path leading up to them
        rating.add(tuple(path))
        return reachable, rating

    for c in cardinals:
        newX, newY = x+c[0], y+c[1]

        if inRange(newX, newY, rows):
            newVal = rows[newY][newX]
            
            if newVal == val+1:
                newReach, newRating = move(newX, newY, rows, path+[(x,y)])
                reachable = reachable.union(newReach)
                rating = rating.union(newRating)

    return reachable, rating

def part1() -> None:
    rows = []
    trailheads = []
    scores = 0

    with open("Day 10/input.txt") as f:
        for y, line in enumerate(f):
            row = []

            for x, char in enumerate(line.strip()):
                if char != ".":
                    row.append(int(char))
                    if int(char) == 0:
                        trailheads.append((x,y))
                else:
                    row.append(-1)
            rows.append(row)
    
    for trailX, trailY in trailheads:
        scores+=len(move(trailX, trailY, rows)[0]) # Ignore rating

    print("Part 1:", scores)

def part2() -> None:
    rows = []
    trailheads = []
    ratings = 0

    with open("Day 10/input.txt") as f:
        for y, line in enumerate(f):
            row = []

            for x, char in enumerate(line.strip()):
                if char != ".":
                    row.append(int(char))
                    if int(char) == 0:
                        trailheads.append((x,y))
                else:
                    row.append(-1)
            rows.append(row)
    
    for trailX, trailY in trailheads:
        ratings+=len(move(trailX, trailY, rows)[1]) # Ignore score

    print("Part 2:", ratings)

part1()
part2()