import os, datetime
spaces = 4
today = datetime.date.today()
if today.month == 12:
    for i in range(1,today.day+1):
        if not os.path.exists(f"Day {i:02}"):
            os.mkdir(f"Day {i:02}")
            file = open(f"Day {i:02}/day{i:02}.py","w")
            file.write(f'with open("Day {i:02}/input.txt") as f:\n'+' '*spaces)
            file.close()
            file = open(f"Day {i:02}/input.txt","w")
            file.close()
            print(f"Day {i:02} Generated")
            exit(0)
    print("All folders/files up to date")