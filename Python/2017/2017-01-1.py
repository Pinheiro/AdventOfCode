def casptchaSolution(sequence):
    digits = [int(x) for x in sequence]
    matches = []
    size = len(digits)
    for i in range(0, size-1): 
        if digits[i] == digits[i+1]: matches.append(digits[i])
    if digits[size-1] == digits[0]: matches.append(digits[size-1])
    return sum(matches)

assert casptchaSolution("1122") == 3
assert casptchaSolution("1111") == 4
assert casptchaSolution("1234") == 0
assert casptchaSolution("91212129") == 9

fileName = "E:/AdventOfCode/_Input/2017/2017-01.txt"
input = open(fileName, "r").read()
print(casptchaSolution(input))