import copy
import time


def read_data(input_path: str) -> list[dict[str, list[int]]]:
    with open(input_path, "r") as inputs:
        input = inputs.readlines()
    data = [line.strip() for line in input]
    warehouse = []
    switch = False
    move_instructions = ""
    robot_pos = (0, 0)
    for i, line in enumerate(data):
        if line == "":
            switch = True
            continue
        if not switch:
            warehouse.append([char for char in line])
            if "@" in line:
                robot_pos = (i, line.find("@"))
        else:
            move_instructions += line
    return {"map": warehouse, "pos": robot_pos, "inst": move_instructions}


def puzzle_pt_1(data) -> int:
    DIR = {
        "<": (0, -1),
        "^": (-1, 0),
        ">": (0, 1),
        "v": (1, 0),
    }
    ware = data["map"]
    pos = data["pos"]
    inst = data["inst"]
    for move in inst:
        move_dir = DIR[move]
        next_pos = (pos[0] + move_dir[0], pos[1] + move_dir[1])
        if ware[next_pos[0]][next_pos[1]] == ".":
            # Empty space, so move the robot in the direction
            ware[next_pos[0]][next_pos[1]] = "@"
            ware[pos[0]][pos[1]] = "."
            pos = next_pos
        elif ware[next_pos[0]][next_pos[1]] == "O":
            # Box, so attempt to move it, and if succesful move the robot as well
            ware, moved = move_box(ware, move_dir, next_pos)
            if moved:
                ware[next_pos[0]][next_pos[1]] = "@"
                ware[pos[0]][pos[1]] = "."
                pos = next_pos
    return calculate_gps_coord(ware)


def move_box(ware, move_dir, pos):
    next_pos = (pos[0] + move_dir[0], pos[1] + move_dir[1])
    moved = False
    if ware[next_pos[0]][next_pos[1]] == "O":
        # If the next position is also a box, try moving it and if succesful move current box as well
        ware, moved = move_box(ware, move_dir, next_pos)
        if moved:
            ware, moved = move_box(ware, move_dir, pos)
    elif ware[next_pos[0]][next_pos[1]] == ".":
        # Empty space, so now can actually move the box
        ware[next_pos[0]][next_pos[1]] = "O"
        ware[pos[0]][pos[1]] = "."
        pos = next_pos
        moved = True
    return ware, moved


def calculate_gps_coord(ware):
    coords = 0
    for i, row in enumerate(ware):
        for j, col in enumerate(row):
            if col == "O":
                coords += (100 * i) + j
    return coords


def puzzle_pt_2(data) -> int:
    # DIR = {
    #     "<": (0, -1),
    #     "^": (-1, 0),
    #     ">": (0, 1),
    #     "v": (1, 0),
    # }
    # ware = rebuild_map(data["map"])
    # pos = data["pos"]
    # inst = data["inst"]
    # for move in inst:
    #     move_dir = DIR[move]
    #     next_pos = (pos[0] + move_dir[0], pos[1] + move_dir[1])
    #     if ware[next_pos[0]][next_pos[1]] == "#":
    #         print("Nothing")
    #     elif ware[next_pos[0]][next_pos[1]] == ".":
    #         ware[next_pos[0]][next_pos[1]] = "@"
    #         ware[pos[0]][pos[1]] = "."
    #         pos = next_pos
    #     else:
    #         print("Box")
    #         ware, moved = move_box(ware, move_dir, next_pos)
    #         if moved:
    #             ware[next_pos[0]][next_pos[1]] = "@"
    #             ware[pos[0]][pos[1]] = "."
    #             pos = next_pos
    # return calculate_gps_coord(ware)
    return 0


def rebuild_map(ware):
    return ware


if __name__ == "__main__":
    data = read_data("src/advent_of_code/y_2024/day_15/input.txt")
    start_time = time.time()
    pt_1 = puzzle_pt_1(copy.deepcopy(data))
    pt_1_duration = time.time() - start_time
    print(f"Day 15, part 1 result: {pt_1}")
    print(f"Day 15, part 1 duration: {pt_1_duration} s")
    start_time = time.time()
    pt_2 = puzzle_pt_2(copy.deepcopy(data))
    pt_2_duration = time.time() - start_time
    print(f"Day 15, part 2 result: {pt_2}")
    print(f"Day 15, part 2 duration: {pt_2_duration} s")
