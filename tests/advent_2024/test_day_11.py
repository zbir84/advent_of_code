import pytest
from src.advent_of_code.y_2024.day_11.puzzle import puzzle_pt_1, puzzle_pt_2, read_data


@pytest.fixture
def input_file_1(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "input_test_1.txt"
    p.write_text(
        """0 1 10 99 999""",
        encoding="utf-8",
    )
    return p


@pytest.fixture
def input_file_2(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "input_test_2.txt"
    p.write_text(
        """125 17""",
        encoding="utf-8",
    )
    return p


def test_puzzle_day_11_1_1(input_file_1):
    data = read_data(input_file_1)
    assert puzzle_pt_1(data, 1) == 7


@pytest.mark.parametrize(
    "blinks,expected",
    [
        (6, 22),
        (25, 55312),
    ],
)
def test_puzzle_day_11_1_2(input_file_2, blinks, expected):
    data = read_data(input_file_2)
    assert puzzle_pt_1(data, blinks) == expected


def test_puzzle_day_11_2(input_file_2):
    data = read_data(input_file_2)
    assert puzzle_pt_2(data, 6) == 22
