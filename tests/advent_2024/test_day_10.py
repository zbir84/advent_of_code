import pytest
from src.advent_of_code.y_2024.day_10.puzzle import puzzle_pt_1, puzzle_pt_2, read_data


@pytest.fixture
def input_file_1(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "input_test_1.txt"
    p.write_text(
        """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""",
        encoding="utf-8",
    )
    return p


@pytest.fixture
def input_file_2(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "input_test_2.txt"
    p.write_text(
        """3390339
3331398
9992997
6543456
7651987
8761111
9871111""",
        encoding="utf-8",
    )
    return p


def test_puzzle_day_10_1_1(input_file_1):
    data = read_data(input_file_1)
    assert puzzle_pt_1(data) == 36


def test_puzzle_day_10_1_2(input_file_2):
    data = read_data(input_file_2)
    assert puzzle_pt_1(data) == 4


def test_puzzle_day_10_2(input_file_1):
    data = read_data(input_file_1)
    assert puzzle_pt_2(data) == 81
