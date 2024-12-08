def read_data(input_path: str) -> list[list[str]]:
    with open(input_path, "r") as inputs:
        lines = inputs.readlines()
    return [[char for char in line.strip()] for line in lines]


def puzzle(data: list[list[str]]) -> tuple[int, int]:
    answer_1 = 0
    answer_2 = 0
    return answer_1, answer_2


if __name__ == "__main__":
    data = read_data("src/advent_of_code/y_2024/day_09/input.txt")
    pt_1, pt_2 = puzzle(data)
    print(f"Day 9, part 1: {pt_1}")
    print(f"Day 9, part 2: {pt_2}")
