import pytest
from src.advent_of_code.y_2024.day_03.puzzle import puzzle


@pytest.fixture
def test_data():
    return "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def test_puzzle_day_03_p1(test_data):
    assert puzzle(test_data, 1) == 161


def test_puzzle_day_03_p2(test_data):
    assert puzzle(test_data, 2) == 48
