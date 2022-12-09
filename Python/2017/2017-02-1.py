def checksum(fileName):
    input = [[int(y) for y in x.strip().split()] for x in open(fileName, "r").readlines()]
    diff = []
    for row in input:
        diff.append(max(row) - min(row))
    return sum(diff)

assert checksum("E:/AdventOfCode/_Input/2017/2017-02-A.txt") == 18
print(checksum("E:/AdventOfCode/_Input/2017/2017-02.txt"))