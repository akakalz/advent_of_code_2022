from advent_of_code_2022.common import get_input, pad_left


class Day:
    def __init__(self, number: int, input_file: str):
        self.number = number
        self.file_name = input_file
        self.input_data = get_input(input_file)

    def part_1(self):
        return None

    def part_2(self):
        return None

    def __repr__(self):
        return f"Day {pad_left(str(self.number), 2, char='0')}"
