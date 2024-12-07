def read_data(input_path: str) -> str:
    with open(input_path, "r") as inputs:
        map = inputs.readlines()
    return [[char for char in row.replace("\n", "")] for row in map]


def puzzle() -> int:
    return 0


if __name__ == "__main__":
    data = read_data("src/advent_of_code/y_2024/day_07/input.txt")
    pt_1 = puzzle()
    print(f"Day 7, part 1: {pt_1}")
    # print(f"Day 7, part 2: {pt_2}")
