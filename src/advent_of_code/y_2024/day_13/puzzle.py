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


def puzzle_pt_1(data: list[dict]) -> int:
    cost_list = []
    for beh in data:
        max_it = max(
            min(beh["P"][0] // beh["A"][0], beh["P"][1] // beh["A"][1], 100),
            min(beh["P"][0] // beh["B"][0], beh["P"][1] // beh["B"][1], 100),
        )
        cost = 9999
        # optimised brute force :P
        for mult_a in range(max_it, 1, -1):
            for mult_b in range(max_it, 1, -1):
                if beh["P"][0] == (beh["A"][0] * mult_a) + (beh["B"][0] * mult_b) and beh["P"][1] == (
                    beh["A"][1] * mult_a
                ) + (beh["B"][1] * mult_b):
                    if cost > (3 * mult_a) + mult_b:
                        cost = (3 * mult_a) + mult_b
        cost_list.append(cost)
    return sum([cost for cost in cost_list if cost != 9999])


def puzzle_pt_2(data: list[dict]) -> int:
    cost_list = []
    for beh in data:
        beh["P"][0] += 10000000000000
        beh["P"][1] += 10000000000000
        # use math!
        b = ((beh["A"][0] * beh["P"][1]) - (beh["A"][1] * beh["P"][0])) / (
            (beh["A"][0] * beh["B"][1]) - (beh["A"][1] * beh["B"][0])
        )
        a = (beh["P"][0] - (beh["B"][0] * b)) / beh["A"][0]
        if a.is_integer() and b.is_integer():
            cost_list.append(int((3 * a) + b))
    return sum(cost_list)


if __name__ == "__main__":
    data = read_data("src/advent_of_code/y_2024/day_13/input.txt")
    start_time = time.time()
    pt_1 = puzzle_pt_1(copy.deepcopy(data))
    pt_1_duration = time.time() - start_time
    print(f"Day 13, part 1 result: {pt_1}")
    print(f"Day 13, part 1 duration: {pt_1_duration} s")
    start_time = time.time()
    pt_2 = puzzle_pt_2(copy.deepcopy(data))
    pt_2_duration = time.time() - start_time
    print(f"Day 13, part 2 result: {pt_2}")
    print(f"Day 13, part 2 duration: {pt_2_duration} s")
