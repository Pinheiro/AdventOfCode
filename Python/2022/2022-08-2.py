#fileName = "_Input/2022-08-1.inputTestA"
fileName = "_Input/2022-08-1.inputPuzzle"
input = [[int(y) for y in x.strip()] for x in open(fileName, "r").readlines()]

def UpScore():
    r = row-1
    result = 0
    while r >= 0:
        result += 1
        if input[r][col] >= input[row][col]: return result
        r -= 1
    return result

def DownScore():
    r = row+1
    result = 0
    while r < len(input):
        result += 1
        if input[r][col] >= input[row][col]: return result
        r += 1
    return result

def LeftScore():
    c = col-1
    result = 0
    while c >= 0:
        result += 1
        if input[row][c] >= input[row][col]: return result
        c -= 1
    return result

def RightScore():
    c = col+1
    result = 0
    while c < len(input[row]):
        result += 1
        if input[row][c] >= input[row][col]: return result
        c += 1
    return result

highScore = 0
for row in range(0, len(input)):
    for col in range(0, len(input[row])):
        if row == 0: treeScore = 0
        elif row == len(input)-1: treeScore = 0
        elif col == 0: treeScore = 0
        elif col == len(input[row])-1: treeScore = 0
        else: treeScore = UpScore()*DownScore()*LeftScore()*RightScore()
        if treeScore > highScore: highScore = treeScore
print(highScore)