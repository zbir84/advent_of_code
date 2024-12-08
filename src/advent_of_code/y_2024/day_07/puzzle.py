import itertools


def read_data(input_path: str) -> str:
    with open(input_path, "r") as inputs:
        lines = inputs.readlines()
    return [(int(line.split(":")[0]), [int(num) for num in line.split(":")[1].strip().split(" ")]) for line in lines]


def generate_combinations(chars: str, length: int):
    yield from itertools.product(*([chars] * length))


def puzzle(data: list[tuple[int, list[int]]]) -> int:
    answer_1 = 0
    solved_eq = []
    for eq_num, eq in enumerate(data):
        operations = [comb for comb in generate_combinations("+*", len(eq[1]) - 1)]
        for op_comb in operations:
            if evaluate_operators(eq[1], op_comb, eq[0]):
                answer_1 += eq[0]
                solved_eq.append(eq_num)
                break
    answer_2 = answer_1
    # only need to check the unsolved equations
    for eq in [eq for eq_num, eq in enumerate(data) if eq_num not in solved_eq]:
        # we just need to get the operations with "|"
        operations = [comb for comb in generate_combinations("|+*", len(eq[1]) - 1) if "|" in comb]
        for op_comb in operations:
            if evaluate_operators(eq[1], op_comb, eq[0]):
                answer_2 += eq[0]
                break
    return answer_1, answer_2


def concat_nums(num1: int, num2: int) -> int:
    return int(str(num1) + str(num2))


def evaluate_operators(numbers: list[int], op: tuple[int], test_value: int) -> bool:
    result = numbers[0]
    for j in range(1, len(numbers)):
        if op[j - 1] == "+":
            # add
            result += numbers[j]
        elif op[j - 1] == "*":
            # mult
            result *= numbers[j]
        else:
            result = concat_nums(result, numbers[j])
        if result > test_value:
            return False
    if test_value - result == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    data = read_data("src/advent_of_code/y_2024/day_07/input.txt")
    pt_1, pt_2 = puzzle(data)
    print(f"Day 7, part 1: {pt_1}")
    print(f"Day 7, part 2: {pt_2}")
