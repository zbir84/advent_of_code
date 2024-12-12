import copy
import time


def read_data(input_path: str) -> list[int]:
    with open(input_path, "r") as inputs:
        input = inputs.read()
    return [int(char) for char in input.strip().split(" ")]


def puzzle_pt_1(data: list[int], blinks: int) -> int:
    i = 0
    while i < blinks:
        temp_data = [blink(num) for num in data]
        data = [x for num in temp_data for x in num]
        i += 1
    return len(data)


def puzzle_pt_2(data: list[int], blinks) -> int:
    map = {}
    for num in data:
        map[num] = 1
    i = 0
    while i < blinks:
        map_2 = copy.deepcopy(map)
        keys = [key for key in map.keys() if map[key] > 0]
        for key in keys:
            num = map[key]
            map_2[key] -= num
            res = blink(key)
            for val in res:
                map_2[val] = map_2.get(val, 0) + num
        i += 1
        map = map_2
    return sum(map.values())


def blink(num: int) -> list[int]:
    if num == 0:
        return [1]
    elif len(str(num)) % 2 == 0:
        return [int(str(num)[0 : int(len(str(num)) / 2)]), int(str(num)[int(len(str(num)) / 2) :])]
    else:
        return [num * 2024]


if __name__ == "__main__":
    data = read_data("src/advent_of_code/y_2024/day_11/input.txt")
    start_time = time.time()
    pt_1 = puzzle_pt_1(copy.deepcopy(data), 25)
    pt_1_duration = time.time() - start_time
    print(f"Day 11, part 1 result: {pt_1}")
    print(f"Day 11, part 1 duration: {pt_1_duration} s")
    start_time = time.time()
    pt_2 = puzzle_pt_2(copy.deepcopy(data), 75)
    pt_2_duration = time.time() - start_time
    print(f"Day 11, part 2 result: {pt_2}")
    print(f"Day 11, part 2 duration: {pt_2_duration} s")
