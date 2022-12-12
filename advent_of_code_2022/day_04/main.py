from advent_of_code_2022.day import Day


class Day4(Day):
    def part_1(self):
        answer = 0
        for line in self.input_data:
            range_1, range_2 = self.parse_line(line)
            if self.range_in_another(range_1, range_2):
                answer += 1

        return answer

    def part_2(self):
        answer = 0
        for line in self.input_data:
            range_1, range_2 = self.parse_line(line)
            if self.has_overlap(range_1, range_2):
                answer += 1

        return answer

    def parse_line(self, line: str):
        range_1, range_2 = line.split(",")
        range_1 = self.parse_range(range_1)
        range_2 = self.parse_range(range_2)
        return range_1, range_2

    def parse_range(self, str_range: str) -> list:
        begin, end = str_range.split("-")
        return range(int(begin), int(end) + 1)

    def range_in_another(self, range_1: list, range_2: list) -> bool:
        min_1, max_1 = range_1[0], range_1[-1]
        min_2, max_2 = range_2[0], range_2[-1]
        return (min_2 >= min_1 and max_2 <= max_1) or (min_1 >= min_2 and max_1 <= max_2)

    def has_overlap(self, range_1: list, range_2: list) -> bool:
        min_1, max_1 = range_1[0], range_1[-1]
        min_2, max_2 = range_2[0], range_2[-1]
        return any(
            [
                min_1 <= min_2 <= max_1,
                min_2 <= min_1 <= max_2,
                min_1 <= max_2 <= max_1,
                min_2 <= max_1 <= max_2,
            ]
        )
