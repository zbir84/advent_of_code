import copy
import time


def read_data(input_path: str) -> dict:
    with open(input_path, "r") as inputs:
        input = inputs.readlines()
    data = [line.strip() for line in input]
    return data


def puzzle_pt_1(data) -> int:
    print(data)
    return 0


def puzzle_pt_2(data: dict) -> int:
    print(data)
    return 0


if __name__ == "__main__":
    data = read_data("src/advent_of_code/y_2024/day_16/input.txt")
    start_time = time.time()
    pt_1 = puzzle_pt_1(copy.deepcopy(data))
    pt_1_duration = time.time() - start_time
    print(f"Day xx, part 1 result: {pt_1}")
    print(f"Day xx, part 1 duration: {pt_1_duration} s")
    start_time = time.time()
    pt_2 = puzzle_pt_2(copy.deepcopy(data))
    pt_2_duration = time.time() - start_time
    print(f"Day xx, part 2 result: {pt_2}")
    print(f"Day xx, part 2 duration: {pt_2_duration} s")
