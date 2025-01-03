import pytest
from src.advent_of_code.y_2024._template.puzzle import puzzle_pt_1, puzzle_pt_2, read_data


@pytest.fixture
def input_file_1(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "input_test_1.txt"
    p.write_text(
        """""",
        encoding="utf-8",
    )
    return p


def test_puzzle_day_xx_1_1(input_file_1):
    data = read_data(input_file_1)
    assert puzzle_pt_1(data) == 0


def test_puzzle_day_xx_2_1(input_file_1):
    data = read_data(input_file_1)
    assert puzzle_pt_2(data) == 0
