rucksacks = [ord(''.join(set(x[0:len(x)//2]).intersection(x[len(x)//2:]))) for x in open('_Input/2022-03.txt', "r").read().split("\n")]
print(sum([(x-96)if(x>96)else(x-38) for x in rucksacks]))