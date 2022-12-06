def startOfPacketEndsAt(dataStream):
    for i in range(4,len(dataStream)+1):
        if len(set(dataStream[i-4:i])) == len(dataStream[i-4:i]):
            return i

assert startOfPacketEndsAt("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
assert startOfPacketEndsAt("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
assert startOfPacketEndsAt("nppdvjthqldpwncqszvftbrmjlhg") == 6
assert startOfPacketEndsAt("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
assert startOfPacketEndsAt("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11

print(startOfPacketEndsAt(open('_Input/2022-06.txt', "r").read()))