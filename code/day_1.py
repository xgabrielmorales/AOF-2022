FILE = "../input/day_1.txt"


def read_input(file: str) -> str:
    with open(file, mode="r") as f:
        input: str = f.read()
    return input


def solve(input: str) -> tuple[int, int]:
    list_sums: list[int] = []
    max_sum: int = 0
    sums: int = 0

    for cal in input.split("\n"):
        if cal.isnumeric():
            sums += int(cal)
            continue

        list_sums.append(sums)

        if sums > max_sum:
            max_sum = sums

        sums = 0

    top_three = sum(sorted(list_sums)[-3:])

    return (max_sum, top_three)


def main():
    input = read_input(FILE)
    solution = solve(input)

    print(solution)


if __name__ == "__main__":
    main()
