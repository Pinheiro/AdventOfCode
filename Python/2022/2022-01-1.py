filename = '_Input/2022-01.txt';
items = open(filename, "r").readlines()
elves = []
total = 0
for item in items:
    if item == "\n": 
        elves.append(total)
        total = 0
    else:
        total += int(item)
print(max(elves))    