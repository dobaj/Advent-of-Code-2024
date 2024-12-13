from heapq import *
import re
import numpy as np
import sympy as sp

def line_intersection (l1,l2):
    (x1, y1, t1), (x2, y2, t2) = l1,l2

    # Figured out by paper
    b = (x2*t1-t2*x1)/(y1*x2-y2*x1)
    a = (t2-y2*b)/x2

    if int(a) != a or int(b) != b:
        # If not an exact solution
        return 0
    
    return int(3*a+b)

def part1() -> None:
    with open("Day 13/input.txt") as f:
        lines = f.readlines()
        cost = 0
        i = 0

        while i < len(lines):
            # Create 2 systems of equations, can only intersect once
            xs,ys = [], []
            j = i
            while j < len(lines) and j-i < 3:
                matches = re.findall("[XY][=+][0-9]*",lines[j])
                x,y =(tuple(map(lambda x: int(x[2:]), matches)))
                xs.append(x)
                ys.append(y)
                j+=1
            
            cost += line_intersection(xs,ys)
            i+=4

        print("Part 1:", cost)

def part2() -> None:
    with open("Day 13/input.txt") as f:
        lines = f.readlines()
        cost = 0
        i = 0

        while i < len(lines):
            # Create 2 systems of equations, can only intersect once
            xs,ys = [], []
            j = i
            while j < len(lines) and j-i < 3:
                matches = re.findall("[XY][=+][0-9]*",lines[j])
                x,y =(tuple(map(lambda x: int(x[2:]), matches)))
                xs.append(x)
                ys.append(y)
                j+=1

            xs[-1]+=10000000000000
            ys[-1]+=10000000000000

            cost += line_intersection(xs,ys)
            i+=4

        print("Part 2:", cost)

part1()
part2()