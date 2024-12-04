def read_data(input_path: str):
    with open(input_path, "r") as inputs:
        all_lines = inputs.readlines()
    return [[int(number) for number in line.split(' ')] for line in all_lines]

def main():
    with open("src/advent_of_code/2024/day_01/input.txt", "r") as inputs:
        all_lines = inputs.readlines()
    list_1 = sorted([int(line.split("   ")[0]) for line in all_lines])
    list_2 = sorted([int(line.split("   ")[1]) for line in all_lines])
    print(distance(list_1, list_2))
    print(similarity(list_1, list_2))

def distance(list_1: list[int], list_2: list[int]) -> int:
    return sum([abs(el_1 - el_2) for el_1, el_2 in zip(list_1, list_2)])

def similarity(list_1: list[int], list_2: list[int]) -> int:
    return sum([num * list_2.count(num) for num in list_1 if num in list_2])    

if __name__ == "__main__":
    data = read_data("src/advent_of_code/y_2024/day_02/input.txt")
    result_no_damp = puzzle(data, 1)
    result_damp = puzzle(data, 2)
    print(f"Day 2, part 1: {result_no_damp}")
    print(f"Day 2, part 2: {result_damp}")
