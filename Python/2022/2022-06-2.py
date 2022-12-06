def startOfPacketEndsAt(dataStream):
    for i in range(14,len(dataStream)+1):
        if len(set(dataStream[i-14:i])) == len(dataStream[i-14:i]):
            return i

assert startOfPacketEndsAt("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
assert startOfPacketEndsAt("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
assert startOfPacketEndsAt("nppdvjthqldpwncqszvftbrmjlhg") == 23
assert startOfPacketEndsAt("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
assert startOfPacketEndsAt("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26

print(startOfPacketEndsAt(open('_Input/2022-06.txt', "r").read()))