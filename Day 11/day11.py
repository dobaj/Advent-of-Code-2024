stoneMap = {}

def blink(stone: list[int], depthLimit: int, depth: int = 0):
    if depth == depthLimit:
        return 1
    
    if (stone, depthLimit-depth) in stoneMap:
        # If we have reached this point before skip recursion
        return stoneMap[(stone, depthLimit-depth)]
    
    elif stone == 0:
        # Store previous results
        result = blink(1, depthLimit, depth+1)
        stoneMap[(stone, depthLimit-depth)] = result
        return result
    
    elif len(str(stone)) % 2 == 0:
        stone = str(stone)
        stoneLen = len(stone)

        # Store previous results
        result = blink(int(stone[:stoneLen//2]), depthLimit, depth+1)
        result += blink(int(stone[stoneLen//2:]), depthLimit, depth+1)
        stoneMap[(stone, depthLimit-depth)] = result
        return result
    
    else:
        # Store previous results
        result = blink(stone*2024, depthLimit, depth+1)
        stoneMap[(stone, depthLimit-depth)] = result
        return result

def part1() -> None:
    with open("Day 11/input.txt") as f:
        line = f.readline().strip()
        stones = list(map(lambda x: int(x), line.split()))
        stonesLen = 0
        
        for stone in stones:
            stonesLen += blink(stone, 25)

        print("Part 1:", stonesLen)

def part2() -> None:
    with open("Day 11/input.txt") as f:
        line = f.readline().strip()
        stones = list(map(lambda x: int(x), line.split()))
        stonesLen = 0
        
        for stone in stones:
            stonesLen += blink(stone, 75)

        print("Part 2:", stonesLen)

part1()
part2()