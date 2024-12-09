import copy
import time


def read_data(input_path: str) -> list[list[str]]:
    with open(input_path, "r") as inputs:
        input = inputs.read()
    decoded_input = []
    for i, char in enumerate(input):
        if i % 2 == 0:
            char_to_put = f"{int(i/2)}"
        else:
            char_to_put = "."
        decoded_input += [char_to_put] * int(char)
    return decoded_input


def puzzle_pt_1(data: list[str]) -> tuple[int, int]:
    ordered_list = order_the_list(data)
    checksum = count_checksum(ordered_list)
    return checksum


def order_the_list(unordered_list):
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


def puzzle_pt_2(data: list[str]) -> tuple[int, int]:
    ordered_list = order_the_list_files(data)
    checksum = count_checksum(ordered_list)
    return checksum


def order_the_list_files(unordered_list):
    return ["0"]


def count_checksum(ordered_list: list[str]) -> int:
    return sum([i * int(id) for i, id in enumerate(ordered_list)])


if __name__ == "__main__":
    data = read_data("src/advent_of_code/y_2024/day_09/input.txt")
    start_time = time.time()
    pt_1 = puzzle_pt_1(copy.deepcopy(data))
    print(f"Day 9, part 1 result: {pt_1}")
    print(f"Day 9, part 1 duration: {time.time() - start_time} s")
    pt_2 = puzzle_pt_2(copy.deepcopy(data))
    print(f"Day 9, part 2: {pt_2}")
