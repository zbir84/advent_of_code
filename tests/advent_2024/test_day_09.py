import pytest
from src.advent_of_code.y_2024.day_09.puzzle import puzzle_pt_1, puzzle_pt_2, read_data


@pytest.fixture
def input_file_1(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "input_test_1.txt"
    p.write_text(
        """12345""",
        encoding="utf-8",
    )
    return p


@pytest.fixture
def input_file_2(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "input_test_2.txt"
    p.write_text(
        """2333133121414131402""",
        encoding="utf-8",
    )
    return p


def test_puzzle_day_09_1_1(input_file_1):
    data = read_data(input_file_1)
    assert puzzle_pt_1(data) == 60


def test_puzzle_day_09_1_2(input_file_2):
    data = read_data(input_file_2)
    assert puzzle_pt_1(data) == 1928


def test_puzzle_day_09_2(input_file_2):
    data = read_data(input_file_2)
    assert puzzle_pt_2(data) == 2858
