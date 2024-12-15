import copy
import time


def read_data(input_path: str) -> dict:
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


def puzzle_pt_1(data: dict) -> int:
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


def puzzle_pt_2(data: dict) -> int:
    DIR = {
        "<": (0, -1),
        "^": (-1, 0),
        ">": (0, 1),
        "v": (1, 0),
    }
    ware, new_y_pos = rebuild_map(data["map"])
    pos = (data["pos"][0], new_y_pos)
    inst = data["inst"]
    for move in inst:
        move_dir = DIR[move]
        next_pos = (pos[0] + move_dir[0], pos[1] + move_dir[1])
        if ware[next_pos[0]][next_pos[1]] == ".":
            # Empty space, so move the robot in the direction
            ware[next_pos[0]][next_pos[1]] = "@"
            ware[pos[0]][pos[1]] = "."
            pos = next_pos
        elif ware[next_pos[0]][next_pos[1]] in ["[", "]"]:
            # Box, so attempt to move it, and if succesful move the robot as well
            if move in ["<", ">"]:
                # If we're pushing the box horizontally, we can use similar method to the one in pt.1, with a small modification.
                ware, moved = move_box_horizontal(ware, move_dir, next_pos)
            else:
                # If we're pushing the box vertically, we need to consider that that boxes might overlap. In that case need use a special method :P
                if ware[next_pos[0]][next_pos[1]] == "[":
                    pos_l = next_pos
                    pos_r = (next_pos[0], next_pos[1] + 1)
                else:
                    pos_l = (next_pos[0], next_pos[1] - 1)
                    pos_r = next_pos
                ware, moved = move_big_box_vertical(ware, move_dir, pos_l, pos_r)
            if moved:
                ware[next_pos[0]][next_pos[1]] = "@"
                ware[pos[0]][pos[1]] = "."
                pos = next_pos
    return calculate_gps_coord(ware, "[")


def move_box(ware: list[list[str]], move_dir: tuple[int, int], pos: tuple[int, int]) -> tuple[list[list[str]], bool]:
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
        moved = True
    return ware, moved


def calculate_gps_coord(ware: list[list[str]], box_edge: str = "O") -> int:
    coords = 0
    for i, row in enumerate(ware):
        for j, col in enumerate(row):
            if col == box_edge:
                coords += (100 * i) + j
    return coords


def rebuild_map(ware: list[list[str]]) -> tuple[list[list[str]], int]:
    new_ware = []
    new_y = -1
    for row in ware:
        new_row = []
        for space in row:
            if space == "#":
                new_row.append("#")
                new_row.append("#")
            elif space == "O":
                new_row.append("[")
                new_row.append("]")
            elif space == ".":
                new_row.append(".")
                new_row.append(".")
            elif space == "@":
                new_row.append("@")
                new_y = len(new_row) - 1
                new_row.append(".")
        new_ware.append(new_row)
    return new_ware, new_y


def move_box_horizontal(
    ware: list[list[str]], move_dir: tuple[int, int], pos: tuple[int, int]
) -> tuple[list[list[str]], bool]:
    next_pos = (pos[0] + move_dir[0], pos[1] + move_dir[1])
    moved = False
    if ware[next_pos[0]][next_pos[1]] in ["[", "]"]:
        # If the next position is also a box, try moving it and if succesful move current box as well
        ware, moved = move_box_horizontal(ware, move_dir, next_pos)
        if moved:
            ware, moved = move_box_horizontal(ware, move_dir, pos)
    elif ware[next_pos[0]][next_pos[1]] == ".":
        # Empty space, so now can actually move the box
        box_side = ware[pos[0]][pos[1]]
        ware[next_pos[0]][next_pos[1]] = box_side
        ware[pos[0]][pos[1]] = "."
        moved = True
    return ware, moved


def move_big_box_vertical(
    ware: list[list[str]], move_dir: tuple[int, int], pos_l: tuple[int, int], pos_r: tuple[int, int]
) -> tuple[list[list[str]], bool]:
    # pushing boxes vertically, we need to consider pairs of positions, left & right
    next_pos_l = (pos_l[0] + move_dir[0], pos_l[1] + move_dir[1])
    next_pos_r = (pos_r[0] + move_dir[0], pos_r[1] + move_dir[1])
    moved = False
    if ware[next_pos_l[0]][next_pos_l[1]] == ware[pos_l[0]][pos_l[1]]:
        # If the next position is also a box with the same side, we can move them together, similar to the horizontal move
        ware, moved = move_big_box_vertical(ware, move_dir, next_pos_l, next_pos_r)
        if moved:
            ware, moved = move_big_box_vertical(ware, move_dir, pos_l, pos_r)
    elif ware[next_pos_l[0]][next_pos_l[1]] == "." and ware[next_pos_r[0]][next_pos_r[1]] == ".":
        # Empty space on both sides, so now can actually move the box
        box_part_l = ware[pos_l[0]][pos_l[1]]
        box_part_r = ware[pos_r[0]][pos_r[1]]
        ware[next_pos_l[0]][next_pos_l[1]] = box_part_l
        ware[next_pos_r[0]][next_pos_r[1]] = box_part_r
        ware[pos_l[0]][pos_l[1]] = "."
        ware[pos_r[0]][pos_r[1]] = "."
        moved = True
    elif ware[next_pos_l[0]][next_pos_l[1]] != "#" and ware[next_pos_r[0]][next_pos_r[1]] != "#":
        # Cases where we have boxes that aren't vertically aligned
        if ware[next_pos_l[0]][next_pos_l[1]] == "]" and ware[next_pos_r[0]][next_pos_r[1]] == "[":
            # 2 boxes, so need to make double move
            cr_l = ((pos_l[0] + move_dir[0], pos_l[1] - 1 + move_dir[1]), next_pos_l)
            cr_r = (next_pos_r, (pos_r[0] + move_dir[0], pos_r[1] + 1 + move_dir[1]))
            ware_t = copy.deepcopy(ware)
            ware_t, moved_l = move_big_box_vertical(ware_t, move_dir, cr_l[0], cr_l[1])
            ware_t, moved_r = move_big_box_vertical(ware_t, move_dir, cr_r[0], cr_r[1])
            # Only actually move if managed to move both of the boxes
            if moved_l and moved_r:
                ware = ware_t
                ware, moved = move_big_box_vertical(ware, move_dir, pos_l, pos_r)
        # Below is just for cases if we only have 1 not-aligned box on one of the sides
        elif ware[next_pos_l[0]][next_pos_l[1]] == "]":
            next_pos_r = (pos_l[0] + move_dir[0], pos_l[1] - 1 + move_dir[1])
            ware, moved = move_big_box_vertical(ware, move_dir, next_pos_r, next_pos_l)
            if moved:
                ware, moved = move_big_box_vertical(ware, move_dir, pos_l, pos_r)
        else:
            next_pos_l = (pos_r[0] + move_dir[0], pos_r[1] + 1 + move_dir[1])
            ware, moved = move_big_box_vertical(ware, move_dir, next_pos_r, next_pos_l)
            if moved:
                ware, moved = move_big_box_vertical(ware, move_dir, pos_l, pos_r)
    return ware, moved


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
