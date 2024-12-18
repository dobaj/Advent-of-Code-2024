import re

registers = [0,0,0] # A, B, C

def readComboOperand(operand):
    if operand < 4:
        return operand
    else:
        if operand % 4 < 3:
            return registers[operand%4]
        return 0

def adv(i,operand):
    registers[0] = registers[0] // (2 ** readComboOperand(operand))
    return i+2

def bxl(i,operand):
    registers[1] = registers[1] ^ operand
    return i+2

def bst(i,operand):
    registers[1] = readComboOperand(operand) % 8
    return i+2

def jnz(i,operand):
    if registers[0] != 0:
        return operand
    return i+2

def bxc(i,operand):
    registers[1] = registers[1] ^ registers[2]
    return i+2

def out(i,operand):
    return (i+2, str(readComboOperand(operand) % 8))

def bdv(i,operand):
    registers[1] = registers[0] // (2 ** readComboOperand(operand))
    return i+2

def cdv(i,operand):
    registers[2] = registers[0] // (2 ** readComboOperand(operand))
    return i+2

opcodes = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

def part1() -> None:
    with open("Day 17/input.txt") as f:
        allOut = []

        line = f.readline()
        j=0
        while line != "\n":
            registers[j] = int(re.search("[0-9]+", line)[0])
            j+=1
            line = f.readline()

        line = f.readline().split(":")[1].strip().split(",")
        line = list(map(lambda x: int(x), line))
        
        i = 0
        while i < len(line)-1:
            opcode = line[i]
            operand = line[i+1]
            value = opcodes[opcode](i,operand)
            if opcode == 5:
                i, output = value
                allOut.append(str(output))
            else:
                i = value

        print("Part 1:", ",".join(allOut))

def compareLine(allOut, line):
    sum = 0
    for i, elem in enumerate(line):
        if allOut[i] > elem:
            sum+=1
        elif allOut[i] < elem:
            sum-=1
    
    return sum

def findOutput (aVal, targetIndex, line, b, c):
    while True:
        registers[0] = aVal
        registers[1] = b
        registers[2] = c
        i = 0
        allOut = []
        
        while i < len(line)-1:
            opcode = int(line[i])
            operand = int(line[i+1])
            value = opcodes[opcode](i,operand)

            if opcode == 5:
                i, output = value
                allOut.append(output)
            else:
                i = value

            if tuple(allOut) == tuple(line[targetIndex:]):
                # If it matches so far we are good
                if (targetIndex == -len(line)):
                    return aVal
                return findOutput(aVal << 3, targetIndex-1, line, b, c)
            
        aVal+=1

def part2() -> None:
    with open("Day 17/input.txt") as f:
        line = f.readline()
        j=0
        while line != "\n":
            registers[j] = int(re.search("[0-9]+", line)[0])
            j+=1
            line = f.readline()

        line = f.readline().split(":")[1].strip().split(",")

        print("Part 2:", findOutput(0,-1, line, registers[1], registers[2]))

part1()
part2()