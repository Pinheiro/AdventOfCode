from collections import deque
from dataclasses import dataclass

@dataclass
class Position:
    row: int = 0
    col: int = 0
    step: int = 0

    def __eq__(self, other):
        return (self.row == other.row) and (self.col == other.col)

def Find(height):
    for row in range(len(heights)):
        for col in range(len(heights[row])):
            if heights[row][col] == height:
                return row, col 
    return -1, -1

def InRange(position):
    return (0 <= position.row < maxRow) and (0 <= position.col < maxCol)

def AtMostOneHigher(p2, p1):
    return (heights[p2.row][p2.col] <= heights[p1.row][p1.col] + 1)

def FewestSteps():
    queue = deque()
    queue.append(start_position)
    visited = set()
    visited.add(tuple([start_position.row, start_position.col]))
    while queue:
        current_position = queue.popleft()
        if current_position == destination:
            return current_position.step
        for dir in directions:
            new_position = Position(current_position.row + dir[0], current_position.col + dir[1], current_position.step + 1)
            if InRange(new_position):
                if AtMostOneHigher(new_position, current_position):
                    new_coordinates = tuple([new_position.row, new_position.col])
                    if not (new_coordinates in visited):
                        queue.append(new_position)
                        visited.add(new_coordinates)

fileName = 'E:/AdventOfCode/_Input/2022/2022-12.txt'
heights = [[elevation for elevation in line.strip()] for line in open(fileName, 'r').read().splitlines()]
start_position = Position(*Find('S'))
destination = Position(*Find('E'))
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]] # left, right, up, down
maxRow, maxCol = len(heights), len(heights[0])
heights[start_position.row][start_position.col] = 'a'
heights[destination.row][destination.col] = 'z'
start_positions = []
for row in range(len(heights)):
    for col in range(len(heights[row])):
        if heights[row][col] == 'a':
            start_positions.append(Position(row, col))
heights = [[ord(height)-ord('a') for height in row] for row in heights]
steps = []
for start_position in start_positions:
    s = FewestSteps()
    if s != None: steps.append(s)
print(min(steps))