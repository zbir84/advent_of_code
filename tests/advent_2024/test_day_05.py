import pytest
from src.advent_of_code.y_2024.day_05.puzzle import puzzle, read_data


@pytest.fixture
def input_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "input_test.txt"
    p.write_text(
        """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""",
        encoding="utf-8",
    )
    return p


def test_puzzle_day_05(input_file):
    page_rules, updates = read_data(input_file)
    assert puzzle(page_rules, updates) == (143, 123)
