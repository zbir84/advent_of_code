import copy
import time


def read_data(input_path: str):
    with open(input_path, "r") as inputs:
        input = inputs.readlines()
    data = []
    behaviour = {}
    for line in input:
        if "Button A" in line:
            behaviour["A"] = [int(line.split(",")[0].split("X+")[1]), int(line.split(",")[1].split("Y+")[1])]
        elif "Button B" in line:
            behaviour["B"] = [int(line.split(",")[0].split("X+")[1]), int(line.split(",")[1].split("Y+")[1])]
        elif "Prize" in line:
            behaviour["P"] = [int(line.split(",")[0].split("X=")[1]), int(line.split(",")[1].split("Y=")[1])]
            data.append(behaviour)
            behaviour = {}
    return data


def puzzle_pt_1(data) -> int:
    return 0


def puzzle_pt_2(data) -> int:
    return 0


if __name__ == "__main__":
    data = read_data("src/advent_of_code/y_2024/day_14/input.txt")
    start_time = time.time()
    pt_1 = puzzle_pt_1(copy.deepcopy(data))
    pt_1_duration = time.time() - start_time
    print(f"Day 14, part 1 result: {pt_1}")
    print(f"Day 14, part 1 duration: {pt_1_duration} s")
    start_time = time.time()
    pt_2 = puzzle_pt_2(copy.deepcopy(data))
    pt_2_duration = time.time() - start_time
    print(f"Day 14, part 2 result: {pt_2}")
    print(f"Day 14, part 2 duration: {pt_2_duration} s")
