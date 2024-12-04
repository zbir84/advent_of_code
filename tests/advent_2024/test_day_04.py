import pytest
from src.advent_of_code.y_2024.day_04.puzzle import puzzle, find_pattern


@pytest.fixture
def test_data():
    return "MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA\nSMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX"


def test_puzzle_day_04_p1(test_data):
    assert puzzle(test_data, 1) == 18


def test_puzzle_day_04_p2(test_data):
    assert puzzle(test_data, 2) == 9


def test_find_xmas_hor():
    test_data = [
        "XMAS",
        "MXMA",
        "SAMX",
        "XMAS",
    ]
    assert find_pattern(test_data, "XMAS", 0, True, False) == 3


def test_find_xmas_ver():
    test_data = [
        "XMAS",
        "MXMA",
        "AAMX",
        "SMAS",
    ]
    assert find_pattern(test_data, "XMAS", 0, False, False) == 1


def test_find_xmas_diag():
    test_data = [
        "XMAS",
        "MMAA",
        "AMAX",
        "XMAS",
    ]
    assert find_pattern(test_data, "XMAS", 0, False, False) == 3
