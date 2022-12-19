from copy import deepcopy
from math import prod
import json

with open("advent_of_code_2022/input/input_puzzle_11.txt", "r") as f:
    input = f.read().split("\n\n")

input = [[instruction.strip() for instruction in monkey.split("\n")] for monkey in input]

rounds = 20

def populateMonkeys(input):
    monkeys = {}
    for monkey in input:
        name = monkey[0].split(":")[0].strip().lower()
        items = [int(x) for x in monkey[1].split(": ")[1].split(", ")]
        operation = monkey[2].split(" = ")[1].strip().replace("old", "item")
        test = int(monkey[3].split("divisible by ")[1])
        ifTrue = monkey[4].split("throw to ")[1].strip()
        ifFalse = monkey[5].split("throw to")[1].strip()

        monkeys[name] = {
            "items": items,
            "operation": operation,
            "divisor": test,
            "ifTrue": ifTrue,
            "ifFalse": ifFalse,
            "itemsCounted": 0
        }
    return monkeys
monkeys = populateMonkeys(input)

# print(json.dumps(monkeys, indent=4))

mod = prod([a["divisor"] for a in monkeys.values()])

print(f"mod = {mod}")

monkeys0 = deepcopy(monkeys)
for _ in range(rounds):
    for monkey, attributes in monkeys0.items():
        toPop = []
        for i, item in enumerate(attributes["items"]):
            attributes["itemsCounted"] += 1
            exec("item = " + attributes["operation"])
            item = item // 3
            if item % attributes["divisor"] == 0:
                monkeys0[attributes["ifTrue"]]["items"].append(item)
                toPop.append(i)
            else:
                monkeys0[attributes["ifFalse"]]["items"].append(item)
                toPop.append(i)

        for i, index in enumerate(toPop):
            attributes["items"].pop(index - i)

monkeys1 = deepcopy(monkeys)
for round in range(10000):
    for monkey, attributes in monkeys1.items():
        toPop = []
        for i, item in enumerate(attributes["items"]):
            attributes["itemsCounted"] += 1
            exec("item = " + attributes["operation"])
            item %= mod
            if item % attributes["divisor"] == 0:
                monkeys1[attributes["ifTrue"]]["items"].append(item)
                toPop.append(i)
            else:
                monkeys1[attributes["ifFalse"]]["items"].append(item)
                toPop.append(i)

        for i, index in enumerate(toPop):
            attributes["items"].pop(index - i)
    if round == 0:
        print(monkeys1)



monkeys0 = sorted(monkeys0.items(), key = lambda monkey: monkey[1]["itemsCounted"], reverse = True)
monkeys0 = monkeys0[0][1]['itemsCounted'] * monkeys0[1][1]['itemsCounted']
monkeys1 = sorted(monkeys1.items(), key = lambda monkey: monkey[1]["itemsCounted"], reverse = True)
# print(monkeys1)
monkeys1 = monkeys1[0][1]['itemsCounted'] * monkeys1[1][1]['itemsCounted']
print(f"Answer 1: {monkeys0}\nAnswer 2: {monkeys1}")
