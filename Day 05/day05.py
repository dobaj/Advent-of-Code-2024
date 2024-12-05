def checkSolution(numMap, solution):
    good = True
    for (i, num) in enumerate(solution):
        for j in range(0,i):
            if num in numMap and solution[j] in numMap[num]:
                good = False
    return good

def part1() -> None:
    numMap = {}
    sum = 0

    with open("Day 05/input.txt") as f:
        line = f.readline()
        while line != "\n":
            # Store in a map of form number: things it needs to be in front of
            nums = line.strip().split('|')
            
            if int(nums[0]) not in numMap:
                numMap[int(nums[0])] = set()
            numMap[int(nums[0])].add(int(nums[1]))
            
            line = f.readline()
        line = f.readline()

        # Solutions to test
        while line:
            solution = list(map(lambda x: int(x), line.strip().split(',')))
            good = checkSolution(numMap, solution)
            
            if good==True:
                sum+=solution[len(solution)//2]
            
            line = f.readline()
        print("Part 1:", sum)

def part2() -> None:
    numMap = {}
    sum = 0

    with open("Day 05/input.txt") as f:
        line = f.readline()
        while line != "\n":
            # Store in a map of form number: things it needs to be in front of
            nums = line.strip().split('|')
            
            if int(nums[0]) not in numMap:
                numMap[int(nums[0])] = set()
            numMap[int(nums[0])].add(int(nums[1]))
            
            line = f.readline()
        line = f.readline()

        # Solutions to test
        while line:
            solution = list(map(lambda x: int(x), line.strip().split(',')))
            good = checkSolution(numMap, solution)
            
            if good==False:
                # Keep swapping numbers that break rules, not sure why this works with one pass
                for (i, num) in enumerate(solution):
                    for j in range(0,i):
                        if num in numMap and solution[j] in numMap[num]:
                            solution[i], solution[j] = solution[j], solution[i]

                # Add new middle number
                sum+=solution[len(solution)//2]
            
            line = f.readline()
        print("Part 2:", sum)

part1()
part2()