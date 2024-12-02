def part1():
    with open("Day 01/input.txt") as f:
        left, right = [], []
        for line in f:
            numbers = list(map(lambda x: int(x),line.strip().split()))
            left.append(numbers[0])
            right.append(numbers[1])
        left.sort()
        right.sort()

        sum = 0
        for i in range(len(left)):
            sum+=abs(left[i]-right[i])
        print("Part 1:", sum)

def part2():
    with open("Day 01/input.txt") as f:
        left, right = [], []

        for line in f:
            numbers = list(map(lambda x: int(x),line.strip().split()))
            left.append(numbers[0])
            right.append(numbers[1])

        leftDict = {}
        for num in left:
            leftDict[num] = 0

        for num in right:
            if num in leftDict:
                leftDict[num] += 1

        sum = 0
        for num in leftDict.keys():
            sum += num*leftDict[num]
        
        print("Part 2:", sum)


part1()
part2()