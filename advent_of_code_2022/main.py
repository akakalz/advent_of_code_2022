from advent_of_code_2022.common import pad_left
from advent_of_code_2022 import current_day


if __name__ == "__main__":
    for i, Day in enumerate(current_day, start=12):
        d = Day(i, f"advent_of_code_2022/input/input_puzzle_{pad_left(str(i), 2, '0')}.txt")
        print(f"== {str(d)} ====================")
        print(f"    part 1: {d.part_1()}")
        print(f"    part 2: {d.part_2()}")

    print("FIN")
