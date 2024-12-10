def part1() -> None:
    sum = 0

    with open("Day 09/input.txt") as f:
        line = f.readline().strip()
        disk = []
        i = 0
        while line:
            disk+=[i]*int(line[0])
            if len(line) > 1:
                disk+=[-1]*int(line[1])
            line = line[2:]
            i+=1
    
    i = 0
    while i < len(disk):
        if disk[i] == -1:
            # Get the rightmost element
            nextElem = disk.pop()
            while nextElem == -1:
                nextElem = disk.pop()
            
            if i >= len(disk):
                # We have reached the end of the array, put the number back
                disk+=[nextElem]
            else:
                disk[i] = nextElem
        i+=1
    
    for i, num in enumerate(disk):
        sum+=i*num

    print("Part 1:", sum)

def part2() -> None:
    sum = 0

    with open("Day 09/input.txt") as f:
        line = f.readline().strip()
        disk = [] # Keep it condensed
        i = 0
        while line:
            disk+=[(i, int(line[0]))]
            if len(line) > 1:
                disk+=[(-1, int(line[1]))]
            line = line[2:]
            i+=1
    

    # Starting from the back, try to move files into gaps
    i = len(disk)-1
    while i >= 0:
        if disk[i][0] > 0: # Not a space
            blocksize = disk[i][1]

            # Find the first space that fits
            j = 0
            while j < i:
                spacesize = disk[j][1]
                if disk[j][0] == -1 and spacesize >= blocksize:
                    # We can move now
                    disk[j] = disk[i]
                    disk[i] = (-1,blocksize)
                    if spacesize > blocksize:
                        # Split space
                        disk.insert(j+1, (-1, spacesize-blocksize))
                        i+=1
                    break
                j+=1
        i-=1
                
    i = 0
    for (num, count) in disk:
        if num >= 0:
            for j in range(count):
                sum+=i*num
                i+=1
        else:
            i+=count

    print("Part 2:", sum)

part1()
part2()