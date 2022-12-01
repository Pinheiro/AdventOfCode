filename = '_Input/2016-03.txt';

def IsPossible(triangle):
    return (triangle[0]+triangle[1]>triangle[2]) and (triangle[0]+triangle[2]>triangle[1]) and (triangle[1]+triangle[2]>triangle[0]);

assert IsPossible([5, 10, 25]) == False;

possibles = 0;
sides = [[int(line[1:5]), int(line[6:10]), int(line[11:15])] for line in open(filename, "r").readlines()];
t = 0;
while t < (len(sides) - 2):
    for i in range(3):
        if IsPossible([sides[t][i], sides[t+1][i], sides[t+2][i]]): possibles += 1;
    t += 3;
print(possibles);