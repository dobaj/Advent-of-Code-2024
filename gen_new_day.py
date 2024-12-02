import os, datetime
spaces = 4
today = datetime.date.today()

def tab() -> str:
    return ' '*spaces

def partTemplate(part: int) -> str:
    return f'def part{part}() -> None:\n' \
        + tab() + f'with open("Day {i:02}/input.txt") as f:\n' \
        + tab() + tab()+f'print("Part {part}:", None)\n\n'

if today.month == 12:
    for i in range(1,today.day+1):
        if not os.path.exists(f"Day {i:02}"):
            os.mkdir(f"Day {i:02}")
            file = open(f"Day {i:02}/day{i:02}.py","w")
            
            # Write template part 1/2 functions 
            file.write(partTemplate(1))
            file.write(partTemplate(2))
            
            # Call functions
            file.write('part1()\n')
            file.write('part2()')
            
            file.close()
            file = open(f"Day {i:02}/input.txt","w")
            file.close()
            print(f"Day {i:02} Generated")
            exit(0)
    print("All folders up to date")