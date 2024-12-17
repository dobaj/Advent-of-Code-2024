from heapq import *
directions = [(1,0), (0,1), (-1,0), (0,-1)]

def findPath(maze, start, end):
    visited = set() # Past paths
    bestScore = -1
    visitedInPaths = set() # Tiles from shortest paths
    bestVisited = {} # A map of each pos with the shortest route to it
    
    toVisit = [start]
    heapify(toVisit)
    
    while len(toVisit) > 0:
        score,x,y,facing,path = heappop(toVisit)
        newPath = path+[(x,y,facing)]
        
        if bestScore <= 0 or score <= bestScore:
            # Check that this is not longer than the longest path
            if tuple(newPath) not in visited:
                if (x,y,facing) not in bestVisited or bestVisited[(x,y,facing)] == score:
                    # If this pos has already been visited, it should be the same score
                    if (x,y) == end:
                        bestScore = score
                        for (x,y,_) in path:
                            visitedInPaths.add((x,y))
                        continue

                    direction = directions[facing]
                    newX,newY = x+direction[0], y+direction[1]

                    if maze[newY][newX] != "#":
                        if (newX,newY,facing) not in path:
                            heappush(toVisit,(score+1,newX,newY,facing,newPath))

                    # Add turns as well
                    cw = (facing + 1) % len(directions)
                    ccw = (facing - 1) % len(directions)

                    if (x,y,cw) not in path:
                        heappush(toVisit,(score+1000,x,y,cw,newPath))
                    if (x,y,ccw) not in path:
                        heappush(toVisit,(score+1000,x,y,ccw,newPath))
                    
                    # Add the prev past path to visited
                    visited.add(tuple(path))
                    bestVisited[(x,y,facing)] = score

    visitedInPaths.add(end)

    return bestScore, len(visitedInPaths)

def part1() -> None:
    with open("Day 16/input.txt") as f:
        start = (0,0,0,0,[]) # Score, pos, facing, past
        end = (0,0)
        maze = []
        
        y = 0
        for line in f:
            row = []
            for x, char in enumerate(line.strip()):
                if char == "S":
                    start = (0,x,y,0,[])
                    row+="."
                elif char == "E":
                    end = (x,y)
                    row+="."
                else:
                    row+=char
            maze.append(row)
            y+=1

        print("Part 1:", findPath(maze,start,end)[0])

def part2() -> None:
    with open("Day 16/input.txt") as f:
        start = (0,0,0,0,[]) # Score, pos, facing, past
        end = (0,0)
        maze = []
        
        y = 0
        for line in f:
            row = []
            for x, char in enumerate(line.strip()):
                if char == "S":
                    start = (0,x,y,0,[])
                    row+="."
                elif char == "E":
                    end = (x,y)
                    row+="."
                else:
                    row+=char
            maze.append(row)
            y+=1

        print("Part 2:", findPath(maze,start,end)[1])

part1()
part2()