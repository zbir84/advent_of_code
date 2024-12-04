def read_data(input_path: str) -> tuple[list[int], list[int]]:
    with open(input_path, "r") as inputs:
        all_lines = inputs.readlines()
    row_1 = [int(line.split("   ")[0]) for line in all_lines]
    row_2 = [int(line.split("   ")[1]) for line in all_lines]
    return (row_1, row_2)

def puzzle(row_1, row_2, part: int) -> int:
    list_1 = sorted(row_1)
    list_2 = sorted(row_2)
    if part == 1:
        return distance(list_1, list_2)
    else:
        return similarity(list_1, list_2)

def distance(list_1: list[int], list_2: list[int]) -> int:
    return sum([abs(el_1 - el_2) for el_1, el_2 in zip(list_1, list_2)])

def similarity(list_1: list[int], list_2: list[int]) -> int:
    return sum([num * list_2.count(num) for num in list_1 if num in list_2])    

if __name__ == "__main__":
    data_1, data_2 = read_data("src/advent_of_code/y_2024/day_01/input.txt")
    distance = puzzle(data_1, data_2, 1)
    similarity = puzzle(data_1, data_2, 2)
    print(f"Day 1, part 1: {distance}")
    print(f"Day 1, part 2: {similarity}")
