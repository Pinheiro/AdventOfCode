filename = '_Input/2016-01.txt';

import numpy

def HowManyBlocksAway(Sequence):
    position  = 0 + 0j
    direction = 0 + 1j
    for s in Sequence.split(", "):
        if s[0] == 'L':
            direction *= 1j
        else:
            direction *= -1j
        for i in range(0, int(s[1:])):
            position += direction
    return (int(abs(position.real)) + int(abs(position.imag)))

assert HowManyBlocksAway('R2, L3') == 5
assert HowManyBlocksAway('R2, R2, R2') == 2
assert HowManyBlocksAway('R5, L5, R5, R3') == 12
print(HowManyBlocksAway(open(filename, "r").read()))