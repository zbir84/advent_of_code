def read_data(input_path: str) -> str:
    with open(input_path, "r") as inputs:
        print_queue = inputs.readlines()
    page_rules = {}
    updates = []
    for line in print_queue:
        if "|" in line:
            if int(line.split("|")[0]) in page_rules.keys():
                page_rules[int(line.split("|")[0])].append(int(line.split("|")[1]))
            else:
                page_rules[int(line.split("|")[0])] = [int(line.split("|")[1])]
        elif "," in line:
            updates.append([int(num) for num in line.split(",")])
    return page_rules, updates


def puzzle(page_rules: dict[int, list[int]], updates: list[list[int]]) -> tuple[int, int]:
    page_total_correct = 0
    page_total_incorrect = 0
    for update in updates:
        correct, middle_page = middle_count(page_rules, update)
        if correct:
            page_total_correct += middle_page
        else:
            page_total_incorrect += middle_count_incorrect(page_rules, update)
    return page_total_correct, page_total_incorrect


def middle_count(rules: dict[int, list[int]], update: list[int]) -> tuple[bool, int]:
    for i, page in enumerate(update):
        if i != 0 and page in rules.keys():
            for printed_number in update[: i + 1]:
                if printed_number in rules[page]:
                    return False, 0
    return True, update[int(len(update) / 2)]


def middle_count_incorrect(rules: dict[int, list[int]], update: list[int]) -> tuple[bool, int]:
    for i in range(0, len(update) - 1):
        for j in range(i + 1, len(update)):
            if update[j] in rules.keys() and update[i] in rules[update[j]]:
                # swap
                temp = update[i]
                update[i] = update[j]
                update[j] = temp
    return update[int(len(update) / 2)]


if __name__ == "__main__":
    page_rules, updates = read_data("src/advent_of_code/y_2024/day_05/input.txt")
    pt_1, pt_2 = puzzle(page_rules, updates)
    print(f"Day 5, part 1: {pt_1}")
    print(f"Day 5, part 2: {pt_2}")
