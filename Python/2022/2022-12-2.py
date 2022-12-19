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

fileName = 'E:/AdventOfCode/_Input/2022/2022-12.txt'
heights = [[elevation for elevation in line.strip()] for line in open(fileName, 'r').read().splitlines()]
current_position = Position(*Find('S'))
destination = Position(*Find('E'))
queue = deque()
queue.append(current_position)
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]] # left, right, up, down
maxRow, maxCol = len(heights), len(heights[0])
heights[current_position.row][current_position.col] = 'a'
heights[destination.row][destination.col] = 'z'
heights = [[ord(height)-ord('a') for height in row] for row in heights]
visited = set()
visited.add(tuple([current_position.row, current_position.col]))
while queue:
    current_position = queue.popleft()
    print(current_position)
    if current_position == destination:
        print(current_position.step)
        break 
    for dir in directions:
        new_position = Position(current_position.row + dir[0], current_position.col + dir[1], current_position.step + 1)
        print('-> ', new_position, InRange(new_position), end = ' ')
        if InRange(new_position):
            print(AtMostOneHigher(new_position, current_position), end = ' ')
            if AtMostOneHigher(new_position, current_position):
                new_coordinates = tuple([new_position.row, new_position.col])
                print(not (new_coordinates in visited), end = ' ')
                if not (new_coordinates in visited):
                    queue.append(new_position)
                    visited.add(new_coordinates)
        print()