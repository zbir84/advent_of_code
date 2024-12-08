import pytest
from src.advent_of_code.y_2024.day_09.puzzle import puzzle, read_data


@pytest.fixture
def input_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "input_test.txt"
    p.write_text(
        """""",
        encoding="utf-8",
    )
    return p


def test_puzzle_day_09(input_file):
    data = read_data(input_file)
    assert puzzle(data) == (0, 0)
