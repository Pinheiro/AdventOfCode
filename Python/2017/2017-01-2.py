def casptchaSolution(sequence):
    digits = [int(x) for x in sequence]
    matches = []
    size = len(digits)
    half = int(size/2)
    for i in range(0, size): 
        j = i + half
        if j >= size: j -= size
        if digits[i] == digits[j]: matches.append(digits[i])
    return sum(matches)

assert casptchaSolution("1212") == 6
assert casptchaSolution("1221") == 0
assert casptchaSolution("123425") == 4
assert casptchaSolution("123123") == 12
assert casptchaSolution("12131415") == 4

fileName = "E:/AdventOfCode/_Input/2017/2017-01.txt"
input = open(fileName, "r").read()
print(casptchaSolution(input))