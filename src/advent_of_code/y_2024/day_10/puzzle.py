import copy
import time


def read_data(input_path: str) -> list[list[str]]:
    with open(input_path, "r") as inputs:
        input = inputs.readlines()
    return [[int(char) for char in line.strip()] for line in input]


def puzzle_pt_1(data: list[str]) -> int:
    max_i = len(data)
    max_j = len(data[0])
    routes = 0
    for i, row in enumerate(data):
        for j, el in enumerate(row):
            if el == 0:
                routes = find_trails(routes, (i, j), data, max_i, max_j, [])
    return routes


def puzzle_pt_2(data: list[str]) -> int:
    max_i = len(data)
    max_j = len(data[0])
    rating = 0
    for i, row in enumerate(data):
        for j, el in enumerate(row):
            if el == 0:
                rating = find_trails_rating(rating, (i, j), data, max_i, max_j)
    return rating


def find_trails(
    routes: int, pos: tuple[int, int], map: list[list[str]], max_i, max_j, visited_highest: list[tuple[int, int]]
) -> int:
    current_el = map[pos[0]][pos[1]]
    if current_el == 9 and pos not in visited_highest:
        visited_highest.append(pos)
        return routes + 1
    for dir in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        next_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if in_bounds(next_pos, max_i, max_j) and map[next_pos[0]][next_pos[1]] == current_el + 1:
            routes = find_trails(routes, next_pos, map, max_i, max_j, visited_highest)
    return routes


def find_trails_rating(rating: int, pos: tuple[int, int], map: list[list[str]], max_i, max_j) -> int:
    current_el = map[pos[0]][pos[1]]
    if current_el == 9:
        return rating + 1
    for dir in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        next_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if in_bounds(next_pos, max_i, max_j) and map[next_pos[0]][next_pos[1]] == current_el + 1:
            rating = find_trails_rating(rating, next_pos, map, max_i, max_j)
    return rating


def in_bounds(pos: tuple[int, int], max_i: int, max_j: int) -> bool:
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] < max_i and pos[1] < max_j


if __name__ == "__main__":
    data = read_data("src/advent_of_code/y_2024/day_10/input.txt")
    start_time = time.time()
    pt_1 = puzzle_pt_1(copy.deepcopy(data))
    pt_1_duration = time.time() - start_time
    print(f"Day 10, part 1 result: {pt_1}")
    print(f"Day 10, part 1 duration: {pt_1_duration} s")
    start_time = time.time()
    pt_2 = puzzle_pt_2(copy.deepcopy(data))
    pt_2_duration = time.time() - start_time
    print(f"Day 10, part 2 result: {pt_2}")
    print(f"Day 10, part 2 duration: {pt_2_duration} s")
