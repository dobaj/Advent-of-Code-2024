import re

def part1() -> None:
    with open("Day 03/input.txt") as f:
        sum = 0
        for line in f:
            matches = list(re.findall(r'mul\([0-9]+,[0-9]+\)', line))
            
            for mul in matches:
                numbers = list(map(lambda x : int(x), re.findall("[0-9]+", mul)))
                sum += numbers[0]*numbers[1]
        print("Part 1:", sum)

def part2() -> None:
    with open("Day 03/input.txt") as f:
        sum = 0
        enabled = True
        for line in f:
            # Thankfully python regex is in order. Find all mul, dos, and don'ts
            matches = list(re.findall(r'mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)', line))
            
            for match in matches:
                if (match == "do()"):
                    enabled = True
                elif (match == "don't()"):
                    enabled = False
                elif (enabled):
                    numbers = list(map(lambda x : int(x), re.findall("[0-9]+", match)))
                    sum += numbers[0]*numbers[1]
        print("Part 2:", sum)

part1()
part2()