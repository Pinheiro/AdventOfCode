class Monkey:

    def __init__(self, input):
        self.items = [int(x) for x in input[1].split(':')[1].split(',')]
        self.operation = eval('lambda old: ' + input[2].split(':')[1].split('=')[1].strip())
        self.test = int(input[3][19:])
        self.ifTrue = int(input[4][-1])
        self.ifFalse = int(input[5][-1])
        self.inspected = 0

    def TakeTurn(self):
        while self.items:
            self.inspected += 1
            worryLevel = self.operation(self.items.pop(0)) // 3
            throwTo = self.ifTrue if (worryLevel % self.test == 0) else self.ifFalse
            yield worryLevel, throwTo

fileName = 'E:/AdventOfCode/_Input/2022/2022-11.txt'
input = [line.strip() for line in open(fileName, 'r').read().splitlines()]
monkeys = [Monkey(input[x:x + 6]) for x in range(0, len(input), 7)]
for _ in range(20):
    for monkey in monkeys:
        for worryLevel, catcher in monkey.TakeTurn():
            monkeys[catcher].items.append(worryLevel)
monkeyBusiness = sorted([monkey.inspected for monkey in monkeys])
print(monkeyBusiness[-1] * monkeyBusiness[-2])