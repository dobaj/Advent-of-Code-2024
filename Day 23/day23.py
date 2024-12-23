def addConnection(connections, a, b):
    if a in connections:
        connections[a].append(b)
    else:
        connections[a] = [b]
    if b in connections:
        connections[b].append(a)
    else:
        connections[b] = [a]

def connectionCount(connections, a, neighbours):
    connected = connections[a]
    return set(connected).intersection(set(neighbours))

def part1() -> None:
    connections = {}
    sets = set()
    with open("Day 23/input.txt") as f:
        for line in f:
            pcs = line.strip().split('-')
            addConnection(connections, pcs[0], pcs[1])
        
        for pc in connections:
            if pc[0] == "t":
                connectedPCs = connections[pc] 
                for i, other in enumerate(connectedPCs):
                    # Get shared neighbours
                    connectedNeighbours = connectionCount(connections,other,connectedPCs[:i]+connectedPCs[i+1:])
                    for _ in range(len(connectedNeighbours)): 
                        # Add all trios   
                        otherOther = connectedNeighbours.pop()
                        pcGroup = [pc, other, otherOther]
                        pcGroup.sort()

                        sets.add(tuple(pcGroup))
        print("Part 1:", len(sets))

def findLargestConnected(connections, pc, group):
    groups = set()

    for g in group:
        arr = [pc,g]
        arr.sort()
        groups.add(tuple(arr))

    for g in group:
        connected = set(connections[g])
        oldGroups = set()

        for potentialGroup in groups:
            canAdd = True
            
            for pc in potentialGroup:
                if pc not in connected:
                    canAdd = False
                    break

            if canAdd == True:
                # If this pc neighbours all pcs add a group with/without it
                newGroup = list(potentialGroup)+[g]
                newGroup.sort()
                oldGroups.add(tuple(newGroup))
        
        groups = groups.union(oldGroups)

    return max(groups,key=len)
    

def part2() -> None:
    connections = {}

    maxGroup = 0,()
    with open("Day 23/input.txt") as f:
        for line in f:
            pcs = line.strip().split('-')
            addConnection(connections, pcs[0], pcs[1])
        
        maxGroup = 0, []
        for pc in connections:
            # Find maximum group with/without a t-pc
            connectedPCs = connections[pc] 

            group = findLargestConnected(connections,pc,connectedPCs)
            if len(group) > maxGroup[0]:
                maxGroup = len(group), group
            
        print("Part 2:", ",".join(maxGroup[1]))

part1()
part2()