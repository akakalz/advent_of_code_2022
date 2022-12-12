import pytest
from advent_of_code_2022.common import pad_left, get_input


def test_get_input(generic_input_file):
    # arrange
    expected_list = ['1', '2', '3', '4', '5']
    # act
    actual_list = get_input(generic_input_file)
    # assert
    assert actual_list == expected_list


@pytest.mark.parametrize(
    "string,size,char,expected_string", [
        ("1", 2, "0", "01"),
        ("1", 2, "A", "A1"),
        ("11", 2, "0", "11"),
        ("111", 2, "0", "111"),
        ("", 2, "0", "00"),
    ]
)
def test_pad_left(string, size, char, expected_string):
    # arrange
    # act
    actual_string = pad_left(string, size, char)
    # assert
    assert actual_string == expected_string
