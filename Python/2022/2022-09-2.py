from operator import add

class Knot:

    def __init__(self):
        self.position = [0, 0]

    def Follow(self, x, y):

        if (x == self.position[0] + 2) and (y == self.position[1] + 2):
            self.position[0] += 1
            self.position[1] += 1
        elif (x == self.position[0] + 2) and (y == self.position[1] - 2):
            self.position[0] += 1
            self.position[1] -= 1
        elif (x == self.position[0] - 2) and (y == self.position[1] - 2):
            self.position[0] -= 1
            self.position[1] -= 1
        elif (x == self.position[0] - 2) and (y == self.position[1] + 2):
            self.position[0] -= 1
            self.position[1] += 1
        else:
            if x == self.position[0] + 2:
                self.position[0] += 1
                if y == self.position[1] - 1: self.position[1] -= 1
                if y == self.position[1] + 1: self.position[1] += 1
            if x == self.position[0] - 2:
                self.position[0] -= 1
                if y == self.position[1] - 1: self.position[1] -= 1
                if y == self.position[1] + 1: self.position[1] += 1
            if y == self.position[1] + 2:
                self.position[1] += 1
                if x == self.position[0] - 1: self.position[0] -= 1
                if x == self.position[0] + 1: self.position[0] += 1
            if y == self.position[1] - 2:
                self.position[1] -= 1
                if x == self.position[0] - 1: self.position[0] -= 1
                if x == self.position[0] + 1: self.position[0] += 1

rows = 5
cols = 6

def PrintWalkMap(knot):
    print()
    walkMap = [['.' for _ in range(cols)] for _ in range (rows)]
    walkMap[(rows - 1)][0] = "s"
    for k in reversed(range(len(knot))): walkMap[(rows - 1) - knot[k].position[1]][knot[k].position[0]] = str(k)
    for row in walkMap: print(''.join(row))
    print()

def Simulation(numberKnots, fileName):
    knot = [Knot() for _ in range(numberKnots)]
    #PrintWalkMap(knot)
    visited = set()
    for direction, steps in [[x.split()[0], int(x.split()[1])] for x in open(fileName, "r").readlines()]:
        for _ in range(steps):
            knot[0].position = list(map(add, knot[0].position, directions[direction]))  # move the head
            for k in range(1, len(knot)): knot[k].Follow(*knot[k-1].position)    	    # move the other knots
            set.add(visited, tuple(knot[k].position))                                   # record tail position (unique values)
            #PrintWalkMap(knot)
    return len(visited)                                                                 # return  the number of positions visited by the tail

directions = {"U": [0, 1], "D": [0, -1], "L": [-1, 0], "R": [1, 0]}

assert Simulation(2, "E:/AdventOfCode/_Input/2022/2022-09-A.txt") == 13
assert Simulation(10, "E:/AdventOfCode/_Input/2022/2022-09-A.txt") == 1
assert Simulation(10, "E:/AdventOfCode/_Input/2022/2022-09-B.txt") == 36
print(Simulation(10, "E:/AdventOfCode/_Input/2022/2022-09.txt"))