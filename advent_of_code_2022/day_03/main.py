from collections import defaultdict
from advent_of_code_2022.day import Day


class Day3(Day):
    is_lower_offset = {
        True: 96,
        False: 38,
    }

    def part_1(self):
        items = []
        for line in self.input_data:
            bag_1, bag_2 = self.split_string(line)
            set_1, set_2 = set(bag_1), set(bag_2)
            intersection = set_1.intersection(set_2)
            items.append(intersection.pop())
        return sum(ord(x) - self.is_lower_offset[x.islower()] for x in items)

    def part_2(self):
        items = []
        group = 0
        groups = defaultdict(list)
        for i, line in enumerate(self.input_data):
            idx = i + 1
            if not idx % 3:
                groups[group].append(set(line))
                items.append(groups[group][0].intersection(groups[group][1]).intersection(groups[group][2]).pop())
                group += 1
                continue
            groups[group].append(set(line))
        return sum(ord(x) - self.is_lower_offset[x.islower()] for x in items)


    def split_string(self, input_str: str) -> tuple[str, str]:
        length = len(input_str) // 2
        return input_str[:length], input_str[length:]
