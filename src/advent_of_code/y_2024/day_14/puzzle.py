import copy
import time


def read_data(input_path: str) -> list[dict[str, list[int]]]:
    with open(input_path, "r") as inputs:
        input = inputs.readlines()
    data = []
    for line in input:
        robot = {}
        robot["pos"] = [int(line.split(" ")[0][2:].split(",")[0]), int(line.split(" ")[0][2:].split(",")[1])]
        robot["v"] = [int(line.split(" ")[1][2:].split(",")[0]), int(line.split(" ")[1][2:].split(",")[1])]
        data.append(robot)
    return data


def puzzle_pt_1(data: list[dict[str, list[int]]], size: tuple[int, int], steps: int) -> int:
    qc = [0, 0, 0, 0]
    for i in range(0, steps):
        for robot in data:
            new_pos = [robot["pos"][0] + robot["v"][0], robot["pos"][1] + robot["v"][1]]
            if 0 <= new_pos[0] < size[0]:
                robot["pos"][0] = new_pos[0]
            elif new_pos[0] < 0:
                robot["pos"][0] = size[0] + new_pos[0]
            elif new_pos[0] >= size[0]:
                robot["pos"][0] = new_pos[0] - size[0]

            if 0 <= new_pos[1] < size[1]:
                robot["pos"][1] = new_pos[1]
            elif new_pos[1] < 0:
                robot["pos"][1] = size[1] + new_pos[1]
            elif new_pos[1] >= size[1]:
                robot["pos"][1] = new_pos[1] - size[1]
    for robot in data:
        q = calculate_quadrant(robot["pos"], size)
        if q is not None:
            qc[q] += 1
    return qc[0] * qc[1] * qc[2] * qc[3]


def puzzle_pt_2(data: list[dict[str, list[int]]], size: tuple[int, int]) -> int:
    for i in range(0, 10000000):
        counts_x = [0] * size[0]
        counts_y = [0] * size[1]
        for robot in data:
            new_pos = [robot["pos"][0] + robot["v"][0], robot["pos"][1] + robot["v"][1]]
            if 0 <= new_pos[0] < size[0]:
                robot["pos"][0] = new_pos[0]
            elif new_pos[0] < 0:
                robot["pos"][0] = size[0] + new_pos[0]
            elif new_pos[0] >= size[0]:
                robot["pos"][0] = new_pos[0] - size[0]

            if 0 <= new_pos[1] < size[1]:
                robot["pos"][1] = new_pos[1]
            elif new_pos[1] < 0:
                robot["pos"][1] = size[1] + new_pos[1]
            elif new_pos[1] >= size[1]:
                robot["pos"][1] = new_pos[1] - size[1]
            counts_x[robot["pos"][0]] += 1
            counts_y[robot["pos"][1]] += 1
        if max(counts_x) > size[0] / 4 and max(counts_y) > size[1] / 4:
            print(i + 1)
            print_map(data, size)
            return i + 1


def print_map(robots: list[dict[str, list[int]]], size: tuple[int, int]):
    map = [["." for _ in range(0, size[0])] for _ in range(0, size[1])]
    for robot in robots:
        if map[robot["pos"][1]][robot["pos"][0]] == ".":
            map[robot["pos"][1]][robot["pos"][0]] = "1"
        else:
            map[robot["pos"][1]][robot["pos"][0]] = str(int(map[robot["pos"][1]][robot["pos"][0]]) + 1)
    for line in map:
        string = "".join(line)
        print(string)


def calculate_quadrant(pos: list[int], size: tuple[int, int]) -> int:
    if pos[0] < size[0] / 2 - 1:
        if pos[1] < size[1] / 2 - 1:
            return 0
        elif pos[1] > size[1] / 2:
            return 2
    elif pos[0] > size[0] / 2:
        if pos[1] < size[1] / 2 - 1:
            return 1
        elif pos[1] > size[1] / 2:
            return 3
    return None


if __name__ == "__main__":
    data = read_data("src/advent_of_code/y_2024/day_14/input.txt")
    start_time = time.time()
    pt_1 = puzzle_pt_1(copy.deepcopy(data), (101, 103), 100)
    pt_1_duration = time.time() - start_time
    print(f"Day 14, part 1 result: {pt_1}")
    print(f"Day 14, part 1 duration: {pt_1_duration} s")
    start_time = time.time()
    pt_2 = puzzle_pt_2(copy.deepcopy(data), (101, 103))
    pt_2_duration = time.time() - start_time
    print(f"Day 14, part 2 result: {pt_2}")
    print(f"Day 14, part 2 duration: {pt_2_duration} s")
