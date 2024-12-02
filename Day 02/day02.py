def safeDistance(a: int, b: int) -> bool:
    difference = abs(a - b);
    return difference >= 1 and difference <= 3

def checkIncreasing(report: list[int]) -> bool:
    for i in range(len(report)-1):
        a, b = report[i], report[i+1]
        
        if a > b or not safeDistance(a, b):
            break
        if i == len(report)-2 :
            return True

def checkDecreasing(report: list[int]) -> bool:
    for i in range(len(report)-1):
        a, b = report[i], report[i+1]
        
        if a < b or not safeDistance(a, b):
            break
        if i == len(report)-2 :
            return True

def part1():
    safe = 0
    with open("Day 02/input.txt") as f:
        for line in f:
            report = list(map(int, line.strip().split()))
            
            if checkIncreasing(report) or checkDecreasing(report):
                safe+=1
    print("Part 1:", safe)

def part2():
    safe = 0
    with open("Day 02/input.txt") as f:
        for line in f:
            report = list(map(int, line.strip().split()))
            
            for i in range(len(report)):
                #See if it works if this element is removed
                newReport = report.copy()
                del newReport[i]
                if checkDecreasing(newReport) or checkIncreasing(newReport):
                    safe+=1
                    break

    print("Part 2:", safe)

part1()
part2()