def IsFullyContained(pairs):
    pair = [[int(y) for y in x.split("-")] for x in pairs.split(",")]
    if (pair[0][0]>=pair[1][0]) and (pair[0][1]<=pair[1][1]): return 1
    if (pair[1][0]>=pair[0][0]) and (pair[1][1]<=pair[0][1]): return 1
    return 0
input = open('_Input/2022-04.txt', "r").read().split("\n")
contain = map(IsFullyContained, input)
print(sum(contain))