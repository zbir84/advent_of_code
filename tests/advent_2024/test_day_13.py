import pytest
from src.advent_of_code.y_2024.day_13.puzzle import puzzle_pt_1, puzzle_pt_2, read_data


@pytest.fixture
def input_file_1(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "input_test_1.txt"
    p.write_text(
        """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279""",
        encoding="utf-8",
    )
    return p


def test_puzzle_day_13_1_1(input_file_1):
    data = read_data(input_file_1)
    assert puzzle_pt_1(data) == 480


def test_puzzle_day_13_2_1(input_file_1):
    data = read_data(input_file_1)
    assert puzzle_pt_2(data) == 875318608908
