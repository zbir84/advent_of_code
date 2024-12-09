import copy
import time


def read_data(input_path: str) -> list[list[str]]:
    with open(input_path, "r") as inputs:
        input = inputs.read().strip()
    decoded_input = []
    for i, char in enumerate(input):
        if i % 2 == 0:
            char_to_put = f"{int(i/2)}"
        else:
            char_to_put = "."
        decoded_input += [char_to_put] * int(char)
    return decoded_input


def puzzle_pt_1(data: list[str]) -> int:
    ordered_list = order_the_list(data)
    checksum = count_checksum(ordered_list)
    return checksum


def puzzle_pt_2(data: list[str]) -> int:
    ordered_list = order_the_list_files(data)
    checksum = count_checksum(ordered_list)
    return checksum


def order_the_list(unordered_list: list[str]) -> list[str]:
    j = len(unordered_list) - 1
    i = 0
    while i < j:
        if unordered_list[i] == ".":
            unordered_list[i] = unordered_list[j]
            unordered_list[j] = "."
            while unordered_list[j] == ".":
                j -= 1
        i += 1
    return unordered_list[0 : j + 1]


def order_the_list_files(unordered_list: list[str]) -> list[str]:
    loc_file = []
    loc_gaps = {}
    i = 0
    # first get data in a shape to make it easier for processing, file locations and their size in a list
    # gap locations and their length in a map
    while i < len(unordered_list):
        if unordered_list[i] == ".":
            start_loc = i
            while unordered_list[i] == ".":
                loc_gaps[start_loc] = loc_gaps.get(start_loc, 0) + 1
                i = i + 1
        else:
            current_id = unordered_list[i]
            loc_file.append([i, 0])
            while i < len(unordered_list) and unordered_list[i] != ".":
                if current_id != unordered_list[i]:
                    loc_file.append([i, 0])
                    current_id = unordered_list[i]
                loc_file[int(current_id)][1] += 1
                i = i + 1
    j = len(loc_file) - 1
    i = 0
    # for each file, starting from the highest id, check if exists a gap "before" the file that can fit that file
    # if it does, move the file and check the next one.
    while j > 0:
        file_loc = loc_file[j][0]
        file_size = loc_file[j][1]
        matching_keys = []
        for key in loc_gaps.keys():
            if key < file_loc and loc_gaps[key] >= file_size:
                matching_keys.append(key)
        if len(matching_keys) > 0:
            min_key = min(matching_keys)
            space_size = loc_gaps[min_key] - file_size
            # move the file around
            unordered_list[min_key : min_key + file_size] = [f"{j}"] * file_size
            unordered_list[file_loc : file_loc + file_size] = ["."] * file_size
            # remove the existing gap as it's now full
            loc_gaps.pop(min_key)
            if space_size > 0:
                # if there's any space left add a new gap
                loc_gaps[min_key + file_size] = space_size
        j -= 1
    return unordered_list


def count_checksum(ordered_list: list[str]) -> int:
    return sum([i * int(id) for i, id in enumerate(ordered_list) if id != "."])


if __name__ == "__main__":
    data = read_data("src/advent_of_code/y_2024/day_09/input.txt")
    start_time = time.time()
    pt_1 = puzzle_pt_1(copy.deepcopy(data))
    pt_1_duration = time.time() - start_time
    print(f"Day 9, part 1 result: {pt_1}")
    print(f"Day 9, part 1 duration: {pt_1_duration} s")
    start_time = time.time()
    pt_2 = puzzle_pt_2(copy.deepcopy(data))
    pt_2_duration = time.time() - start_time
    print(f"Day 9, part 2: {pt_2}")
    print(f"Day 9, part 2 duration: {pt_2_duration} s")
