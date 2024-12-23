def part1() -> None:
    with open("Day 22/input.txt") as f:
        sum = 0
        
        for line in f:

            secretNum = int(line.strip())
            for i in range(2000):
                secretNum = ((secretNum << 6) ^ secretNum) % 16777216
                secretNum = ((secretNum >> 5) ^ secretNum) % 16777216
                secretNum = ((secretNum << 11) ^ secretNum) % 16777216
            
            sum+=secretNum
        print("Part 1:", sum)

def part2() -> None:
    with open("Day 22/input.txt") as f:
        prices = []
        deltaPrices = []
        for line in f:
            secretNum = int(line.strip())
            monkeyPrices = [secretNum%10]
            deltaMonkeyPrices = []
            
            for i in range(2000):
                secretNum = ((secretNum << 6) ^ secretNum) % 16777216
                secretNum = ((secretNum >> 5) ^ secretNum) % 16777216
                secretNum = ((secretNum << 11) ^ secretNum) % 16777216
               
                price = secretNum % 10

                deltaMonkeyPrices.append(price-monkeyPrices[-1])
                monkeyPrices.append(price)

            prices.append(monkeyPrices)
            deltaPrices.append(deltaMonkeyPrices)
        
        maps = [{} for x in prices] # Sequence: price
        sequences = set()
        for i, monkeyPrices in enumerate(prices):
            for j, price in enumerate(monkeyPrices):
                if j >= 4:
                    # Starting at fourth element
                    sequence = tuple(deltaPrices[i][j-4:j])
                    if sequence not in maps[i]:
                        maps[i][sequence] = price
                    sequences.add(sequence)

        maxBanana = 0
        for s in sequences:
            # Check all sequences to get the best one
            sum = 0
            for m in maps:
                if s in m:
                    sum+=m[s]
            maxBanana = max(sum,maxBanana)
            
        print("Part 2:", maxBanana)

part1()
part2()