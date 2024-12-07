import copy


def read_data(input_path: str) -> str:
    with open(input_path, "r") as inputs:
        map = inputs.readlines()
    return [[char for char in row.replace("\n", "")] for row in map]


def puzzle(map: list[list[str]]) -> tuple[int, int]:
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


def move_and_count(
    start_map: list[list[str]], start_pos: tuple[int, int], start_dir: tuple[int, int]
) -> tuple[int, int]:
    position_map = {
        "-1_0": "<",
        "0_-1": "^",
        "1_0": ">",
        "0_1": "v",
    }
    edge = False
    visited_map = []
    loop_obstruction = []
    cp = start_pos
    cd = start_dir
    map = copy.deepcopy(start_map)
    while not edge:
        visited_map.append(cp)
        edge, cp, cd, map = move(cp, cd, map, position_map)
    for pos in visited_map:
        if pos != start_pos and check_loop(start_pos, start_dir, pos, start_map, position_map):
            loop_obstruction.append(pos)
    return len(set(visited_map)), len(set(loop_obstruction))


def move(
    cp: tuple[int, int], cd: tuple[int, int], map: list[list[str]], position_map: dict[str, str]
) -> tuple[bool, tuple[int, int], tuple[int, int], list[list[str]]]:
    next_move = (cp[0] + cd[0], cp[1] + cd[1])
    if not map_bounds(next_move[0], next_move[1], len(map[0]), len(map)):
        return (True, cp, cd, map)
    elif map[next_move[1]][next_move[0]] == ".":
        # move forward
        map[cp[1]][cp[0]] = "."
        cp = next_move
    else:
        # rotate
        temp = (cd[1] * -1, cd[0])
        cd = temp
    map[cp[1]][cp[0]] = position_map[f"{cd[0]}_{cd[1]}"]
    return (False, cp, cd, map)


def map_bounds(x: int, y: int, max_x: int, max_y) -> bool:
    return x >= 0 and x < max_x and y >= 0 and y < max_y


def check_loop(
    cp: tuple[int, int],
    cd: tuple[int, int],
    obstruction: tuple[int, int],
    map: list[list[str]],
    position_map: dict[str, str],
) -> bool:
    temp_map = copy.deepcopy(map)
    temp_map[obstruction[1]][obstruction[0]] = "0"
    visited = set()
    edge = False
    while not edge:
        visited.add(f"{cp[0]}_{cp[1]}_{cd[0]}_{cd[1]}")
        edge, cp, cd, temp_map = move(cp, cd, temp_map, position_map)
        if not edge and f"{cp[0]}_{cp[1]}_{cd[0]}_{cd[1]}" in visited:
            # we're back in the patrol loop
            return True
    return False


if __name__ == "__main__":
    map = read_data("src/advent_of_code/y_2024/day_06/input.txt")
    pt_1, pt_2 = puzzle(map)
    print(f"Day 6, part 1: {pt_1}")
    print(f"Day 6, part 2: {pt_2}")
