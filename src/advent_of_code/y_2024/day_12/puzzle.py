import copy
import time


def read_data(input_path: str) -> list[int]:
    with open(input_path, "r") as inputs:
        input = inputs.readlines()
    return [[letter for letter in line.strip()] for line in input]


def puzzle_pt_1(data: list[list[str]]) -> int:
    DIRECTIONS = {(-1, 0), (0, 1), (0, -1), (1, 0)}
    map = {}
    borders = {}
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            map[(i, j)] = char
    for pos in map.keys():
        borders[pos] = borders.get(pos, set())
        for dir in DIRECTIONS:
            if map[pos] == map.get((pos[0] + dir[0], pos[1] + dir[1]), ""):
                borders[pos].add((pos[0] + dir[0], pos[1] + dir[1]))
    visited = []
    total_price = 0
    for pos in borders.keys():
        bord = []
        if pos not in visited:
            bord, visited = calc_border(pos, borders, bord, visited)
            total_price += len(bord) * sum(bord)
            # print(map[pos], len(bord) * sum(bord))
    return total_price


def puzzle_pt_2(data: list[int]) -> int:
    DIRECTIONS = {(-1, 0), (0, 1), (0, -1), (1, 0)}
    map = {}
    borders = {}
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            map[(i, j)] = char
    for pos in map.keys():
        borders[pos] = borders.get(pos, set())
        for dir in DIRECTIONS:
            if map[pos] == map.get((pos[0] + dir[0], pos[1] + dir[1]), ""):
                borders[pos].add((pos[0] + dir[0], pos[1] + dir[1]))
    visited = []
    total_price = 0
    for pos in borders.keys():
        sides = []
        if pos not in visited:
            sides, visited = calc_sides(pos, borders, sides, visited)
            total_price += len(sides) * sum(sides)
            # print(map[pos], len(bord) * sum(bord))
    return total_price


def calc_border(pos, borders, bord, visited):
    visited.append(pos)
    for next_pos in borders[pos]:
        if next_pos not in visited:
            bord, visited = calc_border(next_pos, borders, bord, visited)
    bord.append(4 - len(borders[pos]))
    return bord, visited


def calc_sides(pos, borders, sides, visited):
    visited.append(pos)
    for next_pos in borders[pos]:
        if next_pos not in visited:
            sides, visited = calc_sides(next_pos, borders, sides, visited)
    sides.append(pos)
    return sides, visited


if __name__ == "__main__":
    data = read_data("src/advent_of_code/y_2024/day_12/input.txt")
    start_time = time.time()
    pt_1 = puzzle_pt_1(copy.deepcopy(data))
    pt_1_duration = time.time() - start_time
    print(f"Day 12, part 1 result: {pt_1}")
    print(f"Day 12, part 1 duration: {pt_1_duration} s")
    start_time = time.time()
    pt_2 = puzzle_pt_2(copy.deepcopy(data))
    pt_2_duration = time.time() - start_time
    print(f"Day 12, part 2 result: {pt_2}")
    print(f"Day 12, part 2 duration: {pt_2_duration} s")
