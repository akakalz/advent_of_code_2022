from advent_of_code_2022.day_09.main import Day9


def test_day9():
    # arrange
    expected = 36
    d = Day9(9, "tests/input/day9.txt")
    # act
    actual = d.part_2()
    # assert
    assert actual == expected, f"{actual}"
