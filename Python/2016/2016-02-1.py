filename = '_Input/2016-02.txt';

def BathroomCode(instructions):
    code = "";
    keypad = [[1,2,3],[4,5,6],[7,8,9]];
    x, y = 1, 1
    for line in instructions.split("\n"):
        for direction in line:
            if (direction == "U") and (x > 0): x -= 1;
            if (direction == "D") and (x < 2): x += 1;
            if (direction == "L") and (y > 0): y -= 1;
            if (direction == "R") and (y < 2): y += 1;
        code = code + str(keypad[x][y]);
    return code;

assert BathroomCode("ULL\nRRDDD\nLURDL\nUUUUD") == "1985";
print(BathroomCode(open(filename, "r").read()));