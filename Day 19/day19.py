visited = {}

def countCombos(towel, subTowels):
    towelLen = len(towel)
    
    if towelLen == 0:
        # Full towel is matched
        return 1

    if towel in visited:
        return visited[towel]
    
    visited[towel] = 0
    for pattern in subTowels:
        size = len(pattern)
        if towelLen >= size and towel[:size] == pattern:
            # If pattern matches count combos of the rest of the string
            val = countCombos(towel[size:], subTowels)
            visited[towel] += val

    return visited[towel]

def part1() -> None:
    with open("Day 19/input.txt") as f:
        patterns = f.readline().strip().split(", ")
        sum = 0

        f.readline()
        for line in f.readlines():
            if (countCombos(line.strip(), patterns) > 0):
                sum+=1
        print("Part 1:", sum)

def part2() -> None:
    with open("Day 19/input.txt") as f:
        patterns = f.readline().strip().split(", ")
        sum = 0

        f.readline()
        for line in f.readlines():
            sum+=countCombos(line.strip(), patterns)

        print("Part 2:", sum)

part1()
part2()