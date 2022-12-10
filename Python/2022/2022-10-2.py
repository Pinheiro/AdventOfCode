def Draws(): return (cycle % 40 >= X) and (cycle % 40 <= X + 2)
takes = {'addx': 2, 'noop': 1}
X = 1
cycle = 0
for instruction in [x.split() for x in open('E:/AdventOfCode/_Input/2022/2022-10.txt', 'r').readlines()]:
    for _ in range(takes[instruction[0]]):
        cycle += 1
        print('#', end = '') if Draws() else print('.', end = '')
        if cycle % 40 == 0: print()
    if len(instruction) == 2: X += int(instruction[1])