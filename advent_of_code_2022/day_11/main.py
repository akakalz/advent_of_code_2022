from math import prod
from typing import Callable
from advent_of_code_2022.day import Day
import json


class Test:
    def __init__(self, test_div: int, result_map: dict) -> None:
        self.test_div = test_div
        self.result_map = result_map

    def __repr__(self) -> str:
        return f"Test({self.test_div}, {json.dumps(self.result_map, default=str)})"


class Item:
    def __init__(self, worry_level: int) -> None:
        self.worry_level = worry_level

    def __repr__(self) -> str:
        return f"Item({self.worry_level})"


class Monkey:
    def __init__(self, items: list[Item], operation: Callable, test: Test, gets_bored: bool = True) -> None:
        self.items = items
        self.operation = operation
        self.test = test
        self.gets_bored = gets_bored

        self.inspection_count = 0

    def __repr__(self) -> str:
        return f"Monkey({self.items}, {self.test}, {self.inspection_count})"

    def bored(self, item: Item, global_div: int) -> None:
        if self.gets_bored:
            item.worry_level //= 3
        else:
            item.worry_level %= global_div

    def throw_item_to_monkey(self, item_index: int, monkey: "Monkey") -> None:
        monkey.items.append(self.items[item_index])

    def test_item(self, item: Item) -> bool:
        return not item.worry_level % self.test.test_div


class Day11(Day):
    def part_1(self):
        monkies = self.parse_monkies(monkies_get_bored=True)
        global_div = prod(x.test.test_div for x in monkies.values())
        for round in range(1, 21):
            self.play_round(round, monkies, global_div)
        top_inspectors = sorted(m.inspection_count for m in monkies.values())
        return prod(top_inspectors[-2:])

    def part_2(self):
        monkies = self.parse_monkies(monkies_get_bored=False)
        global_div = prod(x.test.test_div for x in monkies.values())
        for round in range(1, 10_001):
            self.play_round(round, monkies, global_div)
        top_inspectors = sorted(m.inspection_count for m in monkies.values())
        return prod(top_inspectors[-2:])

    def parse_monkies(self, monkies_get_bored: bool = True) -> dict:
        monkies = {}
        monkey_count = 0
        items, operation, test, test_div, true_map, false_map = None, None, None, None, None, None

        for line in self.input_data:
            if not line:
                test = Test(test_div, {True: true_map, False: false_map})
                monkies[monkey_count] = Monkey(items, operation, test, gets_bored=monkies_get_bored)
                monkey_count += 1
            if line.startswith("Monkey"):
                continue
            if line.startswith("  Starting items: "):
                items = [Item(int(x)) for x in line.replace("  Starting items: ", "").split(", ")]
                continue
            if line.startswith("  Operation: "):
                raw_op = line.split(" ")[-2:]
                operation = self.create_adjustment_operation(raw_op[0], raw_op[1])
                continue
            if line.startswith("  Test: "):
                test_div = int(line.split(" ")[-1])
                continue
            if line.startswith("    If true: "):
                true_map = int(line.split(" ")[-1])
                continue
            if line.startswith("    If false: "):
                false_map = int(line.split(" ")[-1])
                continue
        # last monkey
        test = Test(test_div, {True: true_map, False: false_map})
        monkies[monkey_count] = Monkey(items, operation, test, gets_bored=monkies_get_bored)
        return monkies

    def create_adjustment_operation(self, operator: str, adjust_value: str) -> Callable:
        if adjust_value == "old":
            adjust_value = None

        if operator == "*" and adjust_value is not None:
            def _multiply(item: Item) -> None:
                item.worry_level *= int(adjust_value)
            return _multiply
        if operator == "+":
            def _add(item: Item) -> None:
                item.worry_level += int(adjust_value)
            return _add
        if operator == "*" and adjust_value is None:
            def _square(item: Item) -> None:
                item.worry_level *= item.worry_level
            return _square

    def play_round(self, round: int, monkies: dict[int, Monkey], global_div: int) -> None:
        for m_num in monkies:
            monkey = monkies[m_num]
            for idx, item in enumerate(monkey.items):
                orig_value = item.worry_level
                monkey.inspection_count += 1
                monkey.operation(item)
                monkey.bored(item, global_div)
                target_monkey_num = monkey.test.result_map[monkey.test_item(item)]
                target_monkey = monkies[target_monkey_num]
                monkey.throw_item_to_monkey(idx, target_monkey)
            monkey.items = []
