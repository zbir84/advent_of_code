import pytest
from src.advent_of_code.y_2024.day_01.puzzle import puzzle

@pytest.fixture
def test_data():
    return (
        [3, 4, 2, 1, 3, 3],
        [4, 3, 5, 3, 9, 3],
    )

def test_puzzle_day_01_p1(test_data):
    assert puzzle(test_data[0], test_data[1], 1) == 11

def test_puzzle_day_01_p2(test_data):
    assert puzzle(test_data[0], test_data[1], 2) == 31
