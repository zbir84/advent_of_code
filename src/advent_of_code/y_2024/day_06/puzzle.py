def read_data(input_path: str) -> str:
    with open(input_path, "r") as inputs:
        map = inputs.readlines()
    return [[char for char in row.replace("\n", "")] for row in map]


def puzzle(map: list[str]) -> int:
    pos, dir = get_initial_position_and_direction(map)
    count = move_and_count(
        map,
        pos,
        dir,
    )
    return count


def get_initial_position_and_direction(map: list[str]) -> tuple[tuple[int, int], tuple[int, int]]:
    position_map = {
        "^": (0, -1),
        ">": (1, 0),
        "v": (0, 1),
        "<": (-1, 0),
    }
    for i, line in enumerate(map):
        for j, char in enumerate(line):
            if char not in [".", "#"]:
                return (j, i), position_map[char]


def move_and_count(map, cp, cd):
    position_map = {
        "-1_0": "<",
        "0_-1": "^",
        "1_0": ">",
        "0_1": "v",
    }
    edge = False
    visited_map = []
    visited_dir = []
    loop_obstruction = []
    while not edge:
        obs_flag = check_loop(cp, cd, visited_map, visited_dir, map)
        visited_map.append(cp)
        visited_dir.append(f"{cp[0]}_{cp[1]}_{cd[0]}_{cd[1]}")
        edge, cp, cd, map = move(cp, cd, map, position_map)
        if obs_flag:
            loop_obstruction.append(cp)
    return len(set(visited_map)), len(set(loop_obstruction))


def move(cp, cd, map, position_map):
    next_move = (cp[0] + cd[0], cp[1] + cd[1])
    if next_move[0] < 0 or next_move[0] == len(map[0]) or next_move[1] < 0 or next_move[1] == len(map):
        return (True, cp, cd, map)
    elif map[next_move[1]][next_move[0]] == ".":
        map[cp[1]][cp[0]] = "."
        cp = next_move
        map[cp[1]][cp[0]] = position_map[f"{cd[0]}_{cd[1]}"]
        return (False, cp, cd, map)
    else:
        temp = (cd[1] * -1, cd[0])
        cd = temp
        return move(cp, cd, map, position_map)


def check_loop(cp, cd, visited_map, visited_dir, map) -> bool:
    if cp in visited_map:
        # calculate
        temp = (cd[1] * -1, cd[0])
        next_move = (cp[0] + temp[0], cp[1] + temp[1])
        if f"{next_move[0]}_{next_move[1]}_{temp[0]}_{temp[1]}" in visited_dir:
            print("We've got a loop")
            return True
    return False


if __name__ == "__main__":
    map = read_data("src/advent_of_code/y_2024/day_06/input.txt")
    pt_1, pt_2 = puzzle(map)
    print(f"Day 6, part 1: {pt_1}")
    print(f"Day 6, part 2: {pt_2}")
