from collections import deque
from advent_of_code_2022.day import Day


class Day6(Day):
    def part_1(self):
        return self.get_start_sequence_char_location(4)

    def part_2(self):
        return self.get_start_sequence_char_location(14)

    def get_start_sequence_char_location(self, distinct_length: int) -> int:
        marker = 0
        queue = deque(maxlen=distinct_length)
        for line in self.input_data:  # one line in this one
            for char in line:
                queue.append(char)
                marker += 1
                test_set = set(queue)
                if len(test_set) == distinct_length:
                    break
        return marker
