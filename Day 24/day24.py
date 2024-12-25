from heapq import *

def findValues(toVisit: list, operations: dict, values: dict):
    visited = values.copy()

    toVisit = toVisit.copy()
    heapify(toVisit)

    while len(toVisit) > 0:
        score, gate, (in1, op, in2) = heappop(toVisit)

        if gate in visited:
            continue

        prereq = True
        for i in [in1, in2]:
            if i not in visited:
                heappush(toVisit, (score, i, operations[i]))
                prereq = False
        
        if prereq == False:
            heappush(toVisit, (score+1, gate, (in1, op, in2)))
            continue

        val1, val2 = visited[in1], visited[in2]

        if op == "AND":
            visited[gate] = val1 & val2
        elif op == "XOR":
            visited[gate] = val1 ^ val2
        else:
            visited[gate] = val1 | val2
    
    return visited

def part1() -> None:
    toVisit = []
    operations = {}
    values = {}

    with open("Day 24/input.txt") as f:
        line = f.readline()
        while line != "\n":
            gate, val = line.strip().split(": ")
            val = int(val)

            values[gate] = val
            line = f.readline()

        line = f.readline()
        while line:
            ins, gate = line.strip().split(" -> ") 
            ins = ins.split()

            toVisit.append((0, gate, tuple(ins)))
            operations[gate] = tuple(ins)
            line = f.readline()

    values = findValues(toVisit, operations, values)
    
    # Get all z's
    zs = [x for x in operations if x[0] == "z"]
    zs.sort(reverse=True)

    binary = ""
    for z in zs:
        binary+=str(values[z])

    print("Part 1:", int(binary, base=2))

def findNextOps(operations, gate):
    nextOps = []
    for newGate in operations:
        if gate in operations[newGate]:
            nextOps.append(operations[newGate][1])
    return nextOps

def part2() -> None:
    operations = {}
    values = {}

    issues = set()
    with open("Day 24/input.txt") as f:
        line = f.readline()
        while line != "\n":
            gate, val = line.strip().split(": ")
            val = int(val)

            values[gate] = val
            line = f.readline()

        line = f.readline()
        while line:
            ins, gate = line.strip().split(" -> ") 
            ins = ins.split()

            operations[gate] = tuple(ins)
            line = f.readline()

    for gate in operations:
        # Find the gates that are wrong
        
        in1, op, in2 = operations[gate]
        
        if gate[0] == "z" and op != "XOR" and gate != "z45":
            issues.add(gate)
        
        if in1 in ["x00", "y00"]  and in2 in ["x00", "y00"]:
            continue
        
        nextOps = findNextOps(operations, gate)

        if op == "OR" and "OR" in nextOps:
            issues.add(gate)
        
        if op == "AND" and ("XOR" in nextOps or "AND" in nextOps):
            issues.add(gate)
        
        if gate[0] != "z" and op == "XOR" and "XOR" not in nextOps:
            issues.add(gate)
        
        # sorry i copied this one :(
        if gate[0] != "z" and ("x" not in in1+in2 and "y" not in in1+in2) and op == "XOR":
            issues.add(gate)

    issues = list(issues)
    issues.sort()

    print("Part 2:", ",".join(issues))

part1()
part2()