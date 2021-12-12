from utils.file_utils import get_lines


def part1(input):
    max_length = len(input[0])
    e = epsilon(input)
    g = pow(2, max_length) - 1 - e # inverse the bits : 0b11111 - 0b10110 = 0b01001
    return e * g


def part2(input):
    return 0


def epsilon(input):
    max_length = len(input[0])
    epsilon = ""
    for i in range(max_length):
        epsilon += sumIndex(input, i)
    return int(epsilon, 2)


def sumIndex(input, index):
    somme = sum(int(row[index]) for row in input)
    if somme > len(input) / 2:
        return '1'
    else:
        return '0'


if __name__ == "__main__":
    input_lines = get_lines("day3.txt")
    print(f'Solution 1 : {part1(input_lines)}')
    print(f'Solution 2 : {part2(input_lines)}')
