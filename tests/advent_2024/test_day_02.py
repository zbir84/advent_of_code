import pytest
from src.advent_of_code.y_2024.day_02.puzzle import puzzle, is_safe


@pytest.fixture
def test_data():
    return [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([7, 6, 4, 2, 1], 1),
        ([1, 2, 7, 8, 9], 0),
        ([9, 7, 6, 2, 1], 0),
        ([1, 3, 2, 4, 5], 0),
        ([8, 6, 4, 4, 1], 0),
        ([1, 3, 6, 7, 9], 1),
    ],
)
def test_is_safe_day_02_p1(test_input, expected):
    assert is_safe(test_input, True) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([7, 6, 4, 2, 1], 1),
        ([1, 2, 7, 8, 9], 0),
        ([9, 7, 6, 2, 1], 0),
        ([1, 3, 2, 4, 5], 1),
        ([8, 6, 4, 4, 1], 1),
        ([1, 3, 6, 7, 9], 1),
    ],
)
def test_is_safe_day_02_p2(test_input, expected):
    assert is_safe(test_input, False) == expected


def test_puzzle_day_02_p1(test_data):
    assert puzzle(test_data, 1) == 2


def test_puzzle_day_02_p2(test_data):
    assert puzzle(test_data, 2) == 4
