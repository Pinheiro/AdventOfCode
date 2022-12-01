filename = '_Input/2016-03.txt';

def IsPossible(triangle):
    return (triangle[0]+triangle[1]>triangle[2]) and (triangle[0]+triangle[2]>triangle[1]) and (triangle[1]+triangle[2]>triangle[0]);

assert IsPossible([5, 10, 25]) == False;

possibles = 0;
triangles = [[int(line[1:5]), int(line[6:10]), int(line[11:15])] for line in open(filename, "r").readlines()];
for t in triangles:
    if IsPossible(t): possibles += 1;
print(possibles);