FILE = "../input/day_2.txt"


def read_input(file: str) -> str:
    with open(file, mode="r") as f:
        input: str = f.read()
    return input


def solve_part_1(input: str) -> int:
    socre = {'X': 1, 'Y': 2, 'Z': 3}
    wins = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    equivalent = {'X': 'A', 'Y': 'B', 'Z': 'C'}

    my_score: int = 0
    for line in input.split('\n')[:-1]:
        p1_choice, my_choice = line.split(' ')

        my_counter = wins[p1_choice]

        if my_choice == my_counter:
            my_score += (socre[my_choice] + 0)
        elif equivalent[my_choice] == p1_choice:
            my_score += (socre[my_choice] + 3)
        else:
            my_score += (socre[my_choice] + 6)

    return my_score


def solve_part_2(input: str) -> int:
    wins = {'A': 'C', 'B': 'A', 'C': 'B'}
    loses = {'A': 'B', 'B': 'C', 'C': 'A'}
    socre = {'A': 1, 'B': 2, 'C': 3}

    my_score: int = 0
    for line in input.split('\n')[:-1]:
        p1_choice, means = line.split(' ')

        if means == 'X':
            my_score += (socre[wins[p1_choice]] + 0)
        elif means == 'Y':
            my_score += (socre[p1_choice] + 3)
        else:
            my_score += (socre[loses[p1_choice]] + 6)

    return my_score


def main():
    input = read_input(FILE)
    solution = (solve_part_1(input), solve_part_2(input))

    print(solution)


if __name__ == "__main__":
    main()
