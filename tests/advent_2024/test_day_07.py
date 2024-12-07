import pytest
from src.advent_of_code.y_2024.day_06.puzzle import puzzle, read_data


@pytest.fixture
def input_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "input_test.txt"
    p.write_text(
        """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""",
        encoding="utf-8",
    )
    return p


def test_puzzle_day_07(input_file):
    data = read_data(input_file)
    assert puzzle(data) == 3749
