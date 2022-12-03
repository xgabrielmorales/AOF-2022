FILE = "../input/day_3.txt"


def read_input(file: str) -> str:
    with open(file, mode="r") as f:
        input: str = f.read()
    return input


def solve_part_1(input: str) -> int:
    score: int = 0
    for line in input.split('\n')[:-1]:
        mid = len(line) // 2
        intersection = set(line[:mid]) & set(line[mid:])
        common = list(intersection)[0]

        if common.islower():
            score += ord(common) - 96  # Ascii
        else:
            score += ord(common) - 38  # Ascii

    return score


def solve_part_2(input: str) -> int:
    score: int = 0

    input_lines = input.split('\n')[:-1]

    for index in range(0, len(input_lines), 3):
        b1, b2, b3 = input_lines[index: index + 3]

        intersection = set(b1) & set(b2) & set(b3)
        common = list(intersection)[0]

        if common.islower():
            score += ord(common) - 96  # Ascii
        else:
            score += ord(common) - 38  # Ascii

    return score


def main():
    input = read_input(FILE)
    solution = (solve_part_1(input), solve_part_2(input))

    print(solution)


if __name__ == "__main__":
    main()
