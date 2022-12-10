def MoveTail(xH, yH , xT, yT):
    if (xH == xT - 1) and (yH == yT + 2): return -1, 1
    if (xH == xT + 0) and (yH == yT + 2): return 0, 1
    if (xH == xT + 1) and (yH == yT + 2): return 1, 1
    if (xH == xT - 1) and (yH == yT - 2): return -1, -1
    if (xH == xT + 0) and (yH == yT - 2): return 0, -1
    if (xH == xT + 1) and (yH == yT - 2): return 1, -1
    if (xH == xT + 2) and (yH == yT - 1): return 1, -1
    if (xH == xT + 2) and (yH == yT + 0): return 1, 0
    if (xH == xT + 2) and (yH == yT + 1): return 1, 1
    if (xH == xT - 2) and (yH == yT - 1): return -1, -1
    if (xH == xT - 2) and (yH == yT + 0): return -1, 0
    if (xH == xT - 2) and (yH == yT + 1): return -1, 1
    return 0, 0

def Simulation(fileName):
    input = [[x.split()[0], int(x.split()[1])] for x in open(fileName, "r").readlines()]
    positions = set()
    xH, yH = 0, 0
    xT, yT = 0, 0
    dxT, dyT = 0, 0
    pT = f"{xT},{yT}"
    set.add(positions, pT)
    for direction, steps in input:
        for _ in range(0, steps):
            match direction:
                case "U": yH += 1
                case "D": yH -= 1
                case "L": xH -= 1
                case "R": xH += 1
            dxT, dyT = MoveTail(xH, yH , xT, yT)
            xT += dxT
            yT += dyT
            set.add(positions, f"{xT},{yT}")
    return len(positions)

assert Simulation("E:/AdventOfCode/_Input/2022/2022-09-A.txt") == 13
print(Simulation("E:/AdventOfCode/_Input/2022/2022-09.txt"))