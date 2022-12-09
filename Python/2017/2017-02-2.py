def checksum(fileName):
    input = [[int(y) for y in x.strip().split()] for x in open(fileName, "r").readlines()]
    divisions = []
    for row in input:
        for r in range(0, len(row)):
            n = row.pop(r)
            d = list(filter(lambda x: (x % n == 0), row))
            if (len(d) == 1): divisions.append(d[0] // n)
            row.insert(r, n)
    return sum(divisions)

assert checksum("E:/AdventOfCode/_Input/2017/2017-02-B.txt") == 9
print(checksum("E:/AdventOfCode/_Input/2017/2017-02.txt"))