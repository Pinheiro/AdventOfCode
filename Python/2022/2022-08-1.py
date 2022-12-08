#fileName = "_Input/2022-08-1.inputTestA"
fileName = "_Input/2022-08-1.inputPuzzle"
input = [[int(y) for y in x.strip()] for x in open(fileName, "r").readlines()]

def IsVisibleUp():
    r = row-1
    while r >= 0:
        if input[r][col] >= input[row][col]: return False
        r -= 1
    return True

def IsVisibleDown():
    r = row+1
    while r < len(input):
        if input[r][col] >= input[row][col]: return False
        r += 1
    return True

def IsVisibleLeft():
    c = col-1
    while c >= 0:
        if input[row][c] >= input[row][col]: return False
        c -= 1
    return True

def IsVisibleRight():
    c = col+1
    while c < len(input[row]):
        if input[row][c] >= input[row][col]: return False
        c += 1
    return True

def IsVisible():
    return IsVisibleUp() or IsVisibleDown() or IsVisibleLeft() or IsVisibleRight()

visible = 0
for row in range(0, len(input)):
    for col in range(0, len(input[row])):
        if row == 0: visible +=1
        elif row == len(input)-1: visible +=1
        elif col == 0: visible +=1
        elif col == len(input[row])-1: visible +=1
        elif IsVisible(): visible +=1

print(visible)