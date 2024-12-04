def read_data(input_path: str) -> str:
    with open(input_path, "r") as inputs:
        input_instructions = inputs.read()
    return input_instructions


def puzzle(inputs: str, part: int):
    if part == 1:
        search_pattern = "XMAS"
    else:
        search_pattern = "MAS"
    search_len = len(search_pattern)
    count = 0
    last = False
    input_lines = [line for line in inputs.splitlines()]
    for i in range(0, len(input_lines[0]) - (search_len - 1)):
        sub_mat = get_sub_matrix(input_lines, search_len, i, 0)
        if i == len(input_lines[0]) - search_len:
            last = True
        count = find_pattern(sub_mat, search_pattern, count, True, last, part)
        for j in range(1, len(input_lines) - (search_len - 1)):
            sub_mat = get_sub_matrix(input_lines, search_len, i, j)
            count = find_pattern(sub_mat, search_pattern, count, False, last, part)
    return count


def get_sub_matrix(input, mat_size: int, i, j):
    return [line[i : i + mat_size] for line in input[j : j + mat_size]]


def find_pattern(sub_mat: list[str], pattern: str, count: int, all_horizontal: bool, last: bool, part: int = 1):
    if part == 1:
        inverted = ["".join([x[i] for x in sub_mat]) for i, _ in enumerate(sub_mat)]
        if all_horizontal:
            count += sub_mat.count(pattern) + sub_mat.count(pattern[::-1])
        else:
            count += sub_mat[-1].count(pattern) + sub_mat[-1].count(pattern[::-1])
        if last:
            count += inverted.count(pattern) + inverted.count(pattern[::-1])
        else:
            count += inverted[0].count(pattern) + inverted[0].count(pattern[::-1])
    diag_1 = ""
    diag_2 = ""
    for i, line in enumerate(sub_mat):
        diag_1 = diag_1 + line[i]
        diag_2 = diag_2 + line[len(pattern) - 1 - i]
    if part == 1:
        if diag_1 in [pattern, pattern[::-1]]:
            count += 1
        if diag_2 in [pattern, pattern[::-1]]:
            count += 1
    else:
        if diag_1 in [pattern, pattern[::-1]] and diag_2 in [pattern, pattern[::-1]]:
            count += 1
    return count


if __name__ == "__main__":
    data = read_data("src/advent_of_code/y_2024/day_04/input.txt")
    pt_1 = puzzle(data, 1)
    pt_2 = puzzle(data, 2)
    print(f"Day 4, part 1: {pt_1}")
    print(f"Day 4, part 2: {pt_2}")
