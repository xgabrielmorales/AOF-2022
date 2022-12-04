FILE = "../input/day_4.txt"


def read_input(file: str) -> str:
    with open(file, mode="r") as f:
        input: str = f.read()
    return input


def solve(input: str) -> tuple[int, int]:

    num_fully_contains: int = 0
    num_contians: int = 0

    for line in input.split('\n')[:-1]:
        intervals = line.split(',')

        a, b = map(int, intervals[0].split('-'))
        c, d = map(int, intervals[1].split('-'))

        if (a <= c and b >= d) or (c <= a and d >= b):
            num_fully_contains += 1
            num_contians += 1
        elif (a >= c and a <= d) or (b >= c and b <= d):
            num_contians += 1

    return (num_fully_contains, num_contians)


def main():
    input = read_input(FILE)
    solution = solve(input)

    print(solution)


if __name__ == "__main__":
    main()
