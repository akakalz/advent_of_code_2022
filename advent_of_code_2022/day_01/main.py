from collections import defaultdict
from advent_of_code_2022.day import Day


class Day1(Day):
    def part_1(self):
        elves = defaultdict(int)
        elf = 0
        for line in self.input_data:
            if not line:
                elf += 1
                continue
            elves[elf] += int(line)

        max_calories = -99999999
        for elf, calories in elves.items():
            if calories > max_calories:
                max_calories = calories

        return max_calories

    def part_2(self):
        elves = defaultdict(int)
        elf = 0
        for line in self.input_data:
            if not line:
                elf += 1
                continue
            elves[elf] += int(line)

        top_3 = sum(sorted(elves.values(), reverse=True)[:3])
        return top_3
