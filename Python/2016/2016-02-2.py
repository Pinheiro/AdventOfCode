filename = '_Input/2016-02.txt';

keypad = [[None,None,None,None,None,None,None]
         ,[None,None,None,"1" ,None,None,None]
         ,[None,None,"2" ,"3" ,"4" ,None,None]
         ,[None,"5" ,"6" ,"7" ,"8" ,"9" ,None]
         ,[None,None,"A" ,"B" ,"C" ,None,None]
         ,[None,None,None,"D" ,None,None,None]
         ,[None,None,None,None,None,None,None]];

def NextButton(Row, Col, Direction):
    NewRow = Row;
    NewCol = Col;
    if (Direction == "U"): NewRow -= 1;
    if (Direction == "D"): NewRow += 1;
    if (Direction == "L"): NewCol -= 1;
    if (Direction == "R"): NewCol += 1;
    return NewRow, NewCol, keypad[NewRow][NewCol];

def BathroomCode(instructions):
    code = "";
    r,c = 3,1
    for line in instructions.split("\n"):
        for d in line:
            nr,nc,nb = NextButton(r, c, d);
            if nb is not None:
                r,c = nr,nc
        code = code + str(keypad[r][c]);
    return code;

assert BathroomCode("ULL\nRRDDD\nLURDL\nUUUUD") == "5DB3";
print(BathroomCode(open(filename, "r").read()));