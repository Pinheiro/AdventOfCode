filename = '_Input/2016-01.txt';

import numpy

def FirstLocationYouVisitTwice(Sequence):
    position  = 0 + 0j
    direction = 0 + 1j
    locations = [[0,0]]
    for s in Sequence.split(", "):
        if s[0] == 'L':
            direction *= 1j
        else:
            direction *= -1j
        for i in range(0, int(s[1:])):
            position += direction
            x = int(position.real)
            y = int(position.imag)
            if [x,y] not in locations:
                locations.append([x,y])
            else:
                return (abs(x) + abs(y))

assert FirstLocationYouVisitTwice('R8, R4, R4, R8') == 4
print(FirstLocationYouVisitTwice(open(filename, "r").read()))