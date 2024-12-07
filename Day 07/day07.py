def add(a, b):
    return a + b

def mul(a, b):
    return a * b

operators = [add, mul]

def testEquation(testVal: int, numberList: list):
    if len(numberList) == 2:
        for op in operators:
            if op(numberList[0],numberList[1]) == testVal:
                return True
        # Doesn't match any operators
        return False
    
    for op in operators:
        nextList = numberList[1:]
        nextList[0] = op(numberList[0],numberList[1])
        if testEquation(testVal, nextList):
            return True
    # None of the operators work
    return False

def part1() -> None:
    sum = 0
    with open("Day 07/input.txt") as f:
        for line in f:
            test, numbers = line.split(":")
            numbers = list(map(lambda x: int(x), numbers.strip().split()))
            test = int(test)
            if testEquation(test, numbers):
                sum+=test
        print("Part 1:", sum)

def concat(a, b):
    return int(str(a) + str(b))



def part2() -> None:
    operators.append(concat)
    
    sum = 0
    with open("Day 07/input.txt") as f:
        for line in f:
            test, numbers = line.split(":")
            numbers = list(map(lambda x: int(x), numbers.split()))
            test = int(test)
            
            if testEquation(test, numbers):
                sum+=test
        print("Part 2:", sum)

part1()
part2()