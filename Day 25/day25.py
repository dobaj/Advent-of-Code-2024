def part1() -> None:
    with open("Day 25/input.txt") as f:
        locks = set()
        keys = set()

        
        arr = []
        lock = False
        for line in f:
            if arr == []:
                # See if it is a lock or a key
                if line[0] == "#":
                    lock = True
                else:
                    lock = False
                arr = [0 for _ in range(len(line.strip()))]
                continue
            
            for i in range(len(line.strip())):
                # Add number in each column
                if line[i] == "#":
                    arr[i]+=1

            if line == "\n":
                if lock:
                    locks.add(tuple(arr))
                else:
                    for i in range(len(arr)):
                        arr[i] -= 1
                    keys.add(tuple(arr))
                arr = []
        
        if lock:
            locks.add(tuple(arr))
        else:
            for i in range(len(arr)):
                arr[i] -= 1
            keys.add(tuple(arr))
        
        sum = 0
        for lock in locks:
            for key in keys:
                fail = False
                for i, l in enumerate(lock):
                    if l+key[i] > 5:
                        fail = True
                if not fail:
                    sum+=1

        print("Part 1:", sum)

part1()