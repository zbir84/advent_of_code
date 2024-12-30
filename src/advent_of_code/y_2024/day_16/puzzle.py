import copy
import time
from collections import deque


def read_data(input_path: str) -> dict:
    with open(input_path, "r") as inputs:
        input = inputs.readlines()
    return [[char for char in line.strip()] for line in input]


def puzzle_pt_1(data) -> int:
    DIRECTIONS = {
        (0, 1): ">",
        (1, 0): "V",
        (-1, 0): "<",
        (0, -1): "^",
    }
    end = (0, 0)
    pos = (0, 0)
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if col == "S":
                pos = (i, j)
            elif col == "E":
                end = (i, j)
    # points = 100000000000000
    moves = [">"]
    visited = set()
    plan, moves, _, reached_end = move(data, pos, (0, 1), end, moves, DIRECTIONS, visited)
    return calculate_points(moves)


def move(plan, pos, direct, end, moves, directions, visited: set):
    visited.add(pos)
    if pos == end:
        return moves, True
    possible_directions = get_possible_directions(plan, pos, direct, directions, visited)
    plan_copy = copy.deepcopy(plan)
    moves_copy = copy.deepcopy(moves)
    pos_copy = pos
    for next_pos in possible_directions:
        next_dir = (next_pos[1] - pos[1], next_pos[0] - pos[0])
        moves.append(directions[next_dir])
        plan[next_pos[0]][next_pos[1]] = "S"
        plan[pos[0]][pos[1]] = "."
        pos = next_pos
        plan, moves, pos, reached_end = move(plan, pos, direct, end, moves, directions, visited)
        if reached_end:
            print(moves)
        else:
            plan = plan_copy
            moves = moves_copy
            pos = pos_copy
    plan = plan_copy
    moves = moves_copy
    pos = pos_copy
    return plan, moves, pos, False


def get_possible_directions(plan, pos, cur_dir, DIRECTIONS, visited):
    possible_directions = deque()
    for dir in DIRECTIONS.keys():
        next_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if plan[next_pos[0]][next_pos[1]] == "." and next_pos not in visited:
            possible_directions.append(next_pos)
    return possible_directions


def calculate_points(moves):
    points = 0
    for move in moves:
        if move != "R":
            points += 1
        else:
            points += 1000
    return points


def puzzle_pt_2(data: dict) -> int:
    print(data)
    return 0


if __name__ == "__main__":
    data = read_data("src/advent_of_code/y_2024/day_16/input.txt")
    start_time = time.time()
    pt_1 = puzzle_pt_1(copy.deepcopy(data))
    pt_1_duration = time.time() - start_time
    print(f"Day 16, part 1 result: {pt_1}")
    print(f"Day 16, part 1 duration: {pt_1_duration} s")
    start_time = time.time()
    pt_2 = puzzle_pt_2(copy.deepcopy(data))
    pt_2_duration = time.time() - start_time
    print(f"Day 16, part 2 result: {pt_2}")
    print(f"Day 16, part 2 duration: {pt_2_duration} s")
