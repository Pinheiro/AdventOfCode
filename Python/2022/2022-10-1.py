cycle = 0
X = 1
takes = {"addx": 2, "noop": 1}
interesting = [20, 60, 100, 140, 180, 220]
signalStrength = 0
for instruction in [x.split() for x in open("E:/AdventOfCode/_Input/2022/2022-10.txt", "r").readlines()]:
    for _ in range(takes[instruction[0]]):
        cycle += 1
        if cycle in interesting: signalStrength += cycle * X
    if len(instruction) == 2: X += int(instruction[1])
if cycle in interesting: signalStrength += cycle * X
print(signalStrength)