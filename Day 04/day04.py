def search(word, rows, x, y, xDir, yDir):
    i = 0
    # Iterate through word-search positions
    while i < len(word) and inRange(x,y, rows) and rows[y][x] == word[i]:
        x+=xDir
        y+=yDir
        i+=1
    return i == len(word)

def inRange(x,y, rows):
    maxCols = len(rows[0])
    maxRows = len(rows)
    
    return x >= 0 and x < maxCols and y >= 0 and y < maxRows 

def part1() -> None:
    with open("Day 04/input.txt") as f:
        rows = []
        sum = 0

        for line in f:
            rows.append(line.strip())

        for (i, row) in enumerate(rows):
            for (j, elem) in enumerate(row):
                # Find all X's
                if elem == "X":
                    # Search for word in all directions
                    for x in range(-1,2):
                        for y in range( -1, 2):
                            if y != 0 or x != 0:
                                # As long as there is movement
                                if search("XMAS", rows, j, i, x, y):
                                    sum+=1
        print("Part 1:", sum)

def part2() -> None:
    with open("Day 04/input.txt") as f:
        rows = []
        sum = 0

        for line in f:
            rows.append(line.strip())

        for (i, row) in enumerate(rows):
            for (j, elem) in enumerate(row):
                # Find all M's
                if elem == "M":

                    for x in range(-1,2):
                        for y in range( -1, 2):
                            if y == x and (y != 0 or x != 0):
                                
                                # Search diagonally along axis where x-y is the same
                                if search("MAS", rows, j, i, x, y):
                                    if (x == -1):
                                        # Search across other axis to form X
                                        if search("MAS", rows, j-2, i, 1, -1) or search("MAS", rows, j, i-2, -1, 1):
                                            sum+=1
                                    if (x == 1):
                                        # Search across other axis to form X
                                        if search("MAS", rows, j+2, i, -1, 1) or search("MAS", rows, j, i+2, 1, -1):
                                            sum+=1

        print("Part 2:", sum)

part1()
part2()