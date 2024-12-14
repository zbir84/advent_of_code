import pytest
from src.advent_of_code.y_2024.day_14.puzzle import puzzle_pt_1, puzzle_pt_2, read_data


@pytest.fixture
def input_file_1(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "input_test_1.txt"
    p.write_text(
        """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3""",
        encoding="utf-8",
    )
    return p


def test_puzzle_day_14_1_1(input_file_1):
    data = read_data(input_file_1)
    assert puzzle_pt_1(data, (11, 7), 100) == 12


def test_puzzle_day_14_2_1(input_file_1):
    data = read_data(input_file_1)
    assert puzzle_pt_2(data) == 0
