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
    while not edge:
        visited_map.append(cp)
        edge, cp, cd, map = move(cp, cd, map, position_map)

    return len(set(visited_map))


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


if __name__ == "__main__":
    map = read_data("src/advent_of_code/y_2024/day_06/input.txt")
    pt_1 = puzzle(map)
    print(f"Day 6, part 1: {pt_1}")
    # print(f"Day 6, part 2: {pt_2}")
