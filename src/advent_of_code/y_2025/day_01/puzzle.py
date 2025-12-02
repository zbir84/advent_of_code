import copy
import time


def read_data(input_path: str) -> dict:
    with open(input_path, "r") as inputs:
        input = inputs.readlines()
    data = [line.strip() for line in input]
    return data


def puzzle_pt_1(data) -> int:
    cur = 50
    result = 0
    for instr in data:
        dir = instr[0]
        num = int(instr[1:])
        if dir == "L":
            cur = cur - num
            if cur < 0:
                cur = 100 + cur
        else:
            cur = cur + num
            if cur > 99:
                cur = cur - 100
        # print(cur)
        if cur == 0:
            result += 1
    return result


def puzzle_pt_2(data: dict) -> int:
    print(data)
    return 0


if __name__ == "__main__":
    data = read_data("src/advent_of_code/y_2025/day_01/input.txt")
    start_time = time.time()
    pt_1 = puzzle_pt_1(copy.deepcopy(data))
    pt_1_duration = time.time() - start_time
    print(f"Day 01, part 1 result: {pt_1}")
    print(f"Day 01, part 1 duration: {pt_1_duration} s")
    # start_time = time.time()
    # pt_2 = puzzle_pt_2(copy.deepcopy(data))
    # pt_2_duration = time.time() - start_time
    # print(f"Day 01, part 2 result: {pt_2}")
    # print(f"Day 01, part 2 duration: {pt_2_duration} s")
