# A, 1 = Rock        X = Lose
# B, 2 = Paper       Y = Draw
# C, 3 = Scissors    Z = Win

def ApplyNeed(s):
    if (s[0] == "A") and (s[1] == "X"): return "C"
    if (s[0] == "A") and (s[1] == "Y"): return "A"
    if (s[0] == "A") and (s[1] == "Z"): return "B"
    if (s[0] == "B") and (s[1] == "X"): return "A"
    if (s[0] == "B") and (s[1] == "Y"): return "B"
    if (s[0] == "B") and (s[1] == "Z"): return "C"
    if (s[0] == "C") and (s[1] == "X"): return "B"
    if (s[0] == "C") and (s[1] == "Y"): return "C"
    if (s[0] == "C") and (s[1] == "Z"): return "A"

def ScoreForEachRound(s):
    n = ApplyNeed(s)
    if (s[0] == "A") and (n == "A"): return 4
    if (s[0] == "A") and (n == "B"): return 8
    if (s[0] == "A") and (n == "C"): return 3
    if (s[0] == "B") and (n == "A"): return 1
    if (s[0] == "B") and (n == "B"): return 5
    if (s[0] == "B") and (n == "C"): return 9
    if (s[0] == "C") and (n == "A"): return 7
    if (s[0] == "C") and (n == "B"): return 2
    if (s[0] == "C") and (n == "C"): return 6

def TotalScore(strategy):
    rounds = [x.strip().split(" ") for x in strategy.split("\n")]
    return sum([ScoreForEachRound(s) for s in rounds])

assert TotalScore("A Y\nB X\nC Z") == 12

filename = '_Input/2022-02.txt';
print(TotalScore(open(filename, "r").read()))