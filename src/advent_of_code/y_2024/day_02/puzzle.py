def read_data(input_path: str):
    with open(input_path, "r") as inputs:
        all_lines = inputs.readlines()
    return [[int(number) for number in line.split(" ")] for line in all_lines]


def puzzle(reports: list[list[str]], part: int) -> int:
    result = 0
    el_removed_flag = True if part == 1 else False
    for report in reports:
        result += is_safe(report, el_removed_flag)
    return result


def is_safe(report: list[int], el_removed: bool = False) -> int:
    sub_list = [el_1 - el_2 for el_1, el_2 in zip(report[:-1], report[1:])]
    if (min(sub_list) < 0 and max(sub_list) < 0 and abs(min(sub_list)) <= 3) or (
        min(sub_list) > 0 and max(sub_list) > 0 and abs(max(sub_list)) <= 3
    ):
        return 1
    elif not el_removed:
        for i, _ in enumerate(report):
            if i == 0:
                new_report = report[1:]
            else:
                new_report = report[:i] + report[i + 1 :]
            if is_safe(new_report, True) == 1:
                return 1
    return 0


if __name__ == "__main__":
    data = read_data("src/advent_of_code/y_2024/day_02/input.txt")
    result_no_damp = puzzle(data, 1)
    result_damp = puzzle(data, 2)
    print(f"Day 2, part 1: {result_no_damp}")
    print(f"Day 2, part 2: {result_damp}")
