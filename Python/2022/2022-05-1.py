input = open('_Input/2022-05.txt', "r").read().split("\n")
stacks = 9
storage = [[] for stack in range(stacks)]
stackLines = 8
crates = [[line[i+1] for i in range(0, len(line), 4)] for line in input[0:stackLines]]
for crateLine in crates:
    for stack in range(0,len(crateLine)):
        if (crateLine[stack] != " "):
            storage[stack].append(crateLine[stack])
procedure = [[int(line.split()[1]),int(line.split()[3]),int(line.split()[5])] for line in input[stackLines+2:]]
for p in procedure:
    quantity, fromStack, toStack = p
    for q in range(quantity):
        storage[toStack-1].insert(0, storage[fromStack-1].pop(0))
print(''.join([storage[stack].pop(0) for stack in range(stacks)]))