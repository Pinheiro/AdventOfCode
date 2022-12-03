# A, X, 1 = Rock
# B, Y, 2 = Paper
# C, Z, 3 = Scissors

def ScoreForEachRound(s):
    if (s[0] == "A") and (s[1] == "X"): return 4
    if (s[0] == "A") and (s[1] == "Y"): return 8
    if (s[0] == "A") and (s[1] == "Z"): return 3
    if (s[0] == "B") and (s[1] == "X"): return 1
    if (s[0] == "B") and (s[1] == "Y"): return 5
    if (s[0] == "B") and (s[1] == "Z"): return 9
    if (s[0] == "C") and (s[1] == "X"): return 7
    if (s[0] == "C") and (s[1] == "Y"): return 2
    if (s[0] == "C") and (s[1] == "Z"): return 6

def TotalScore(strategy):
    rounds = [x.strip().split(" ") for x in strategy.split("\n")]
    return sum([ScoreForEachRound(s) for s in rounds])

assert TotalScore("A Y\nB X\nC Z") == 15

filename = '_Input/2022-02.txt';
print(TotalScore(open(filename, "r").read()))