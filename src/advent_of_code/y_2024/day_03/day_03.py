def main():
    with open("src/advent_of_code/3/input.txt", "r") as inputs:
        input_instructions = inputs.read()
    dos = input_instructions.split("do()")
    result = 0
    for do in dos:
        dont = do.split("don\'t()")
        # only apply on first split:
        first_occurence = dont[0].find("mul(")
        result += mul(dont[0][first_occurence:])
    print(result)


def mul(input_text: str) -> int:
    chunk_mul = input_text.split("mul(")
    total = 0
    for chunk in chunk_mul:
        num_1 = ""
        num_2 = ""
        for char in chunk:
            if not char.isnumeric():
                if num_1 != "" and num_2 == "" and char == ",":
                    num_1 = int(num_1)
                    continue
                elif num_2 != "" and char == ")":
                    total += num_1 * int(num_2)
                break
            else:
                if isinstance(num_1, int):
                    num_2 += char
                else:
                    num_1 += char
    return total


if __name__ == "__main__":
    main()
