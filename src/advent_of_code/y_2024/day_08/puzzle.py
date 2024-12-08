def read_data(input_path: str) -> list[list[str]]:
    with open(input_path, "r") as inputs:
        lines = inputs.readlines()
    return [[char for char in line.strip()] for line in lines]


def puzzle(data: list[list[str]]) -> tuple[int, int]:
    antenna_positions = find_antenna_positions(data)
    max_bounds = [len(data) - 1, len(data[0]) - 1]
    antinode_positions = set()
    antinode_positions_frequency = set()
    for antenna in antenna_positions:
        antinode_positions = find_antinodes(antenna_positions[antenna], max_bounds, antinode_positions)
        antinode_positions_frequency = find_antinodes_frequency(
            antenna_positions[antenna], max_bounds, antinode_positions_frequency
        )
    answer_1 = len(antinode_positions)
    answer_2 = len(antinode_positions_frequency)
    return answer_1, answer_2


def find_antenna_positions(data: list[list[str]]) -> dict[str, list[tuple[int, int]]]:
    positions = dict()
    for i, row in enumerate(data):
        for j, _ in enumerate(row):
            if data[i][j] != ".":
                positions[data[i][j]] = positions.get(data[i][j], list())
                positions[data[i][j]].append((i, j))
    return positions


def find_antinodes(
    antennas: list[tuple[int, int]], max_bounds: list[int], antinode_positions: set[tuple[int, int]]
) -> set[tuple[int, int]]:
    for i in range(0, len(antennas) - 1):
        for j in range(i + 1, len(antennas)):
            ant_1, ant_2 = calc_antinode(antennas[i], antennas[j])
            if check_bounds(ant_1, max_bounds):
                antinode_positions.add(ant_1)
            if check_bounds(ant_2, max_bounds):
                antinode_positions.add(ant_2)
    return antinode_positions


def find_antinodes_frequency(
    antennas: list[tuple[int, int]], max_bounds: list[int], antinode_positions: set[tuple[int, int]]
) -> set[tuple[int, int]]:
    for i in range(0, len(antennas) - 1):
        for j in range(i + 1, len(antennas)):
            antenna_1 = antennas[i]
            antenna_2 = antennas[j]
            antinode_1, antindode_2 = calc_antinode(antenna_1, antenna_2)
            bounds = 0
            direction = 1
            change_direction = False
            while bounds < 4:
                ant_1, ant_2 = calc_antinode(antenna_1, antenna_2)
                if check_bounds(ant_1, max_bounds):
                    antinode_positions.add(ant_1)
                else:
                    bounds += 1
                    if bounds == 2:
                        change_direction = True
                if check_bounds(ant_2, max_bounds):
                    antinode_positions.add(ant_2)
                else:
                    bounds += 1
                if direction == 1 and not change_direction:
                    antenna_2 = antenna_1
                    antenna_1 = ant_1
                if direction == 2 and not change_direction:
                    antenna_1 = antenna_2
                    antenna_2 = ant_2
                if change_direction:
                    direction = 2
                    change_direction = False
                    antenna_1 = antennas[j]
                    antenna_2 = antindode_2
    return antinode_positions


def calc_antinode(pt1: tuple[int, int], pt2: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
    diff_i = pt1[0] - pt2[0]
    diff_j = pt1[1] - pt2[1]
    return (pt1[0] + diff_i, pt1[1] + diff_j), (pt2[0] - diff_i, pt2[1] - diff_j)


def check_bounds(pt: tuple[int, int], max_bounds: list[int, int]) -> bool:
    return pt[0] >= 0 and pt[1] >= 0 and pt[0] <= max_bounds[0] and pt[1] <= max_bounds[1]


if __name__ == "__main__":
    data = read_data("src/advent_of_code/y_2024/day_08/input.txt")
    pt_1, pt_2 = puzzle(data)
    print(f"Day 8, part 1: {pt_1}")
    print(f"Day 8, part 2: {pt_2}")
