input = open('_Input/2022-03.txt', "r").read().split("\n")
badges = [ord(list(set.intersection(*map(set,input[n:n+3])))[0]) for n in range(0, len(input), 3)]
print(sum([(x-96)if(x>96)else(x-38) for x in badges]))