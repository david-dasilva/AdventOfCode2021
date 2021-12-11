from utils.file_utils import get_lines


def part1(input):
    commands = getCommands(input)
    xpos = 0
    depth = 0

    for command in commands:
        match command:
            case ('up', amount):
                depth -= amount
            case ('down', amount):
                depth += amount
            case ('forward', amount):
                xpos += amount

    return xpos * depth


def part2(input):
    commands = getCommands(input)
    xpos = 0
    depth = 0
    aim = 0
    for command in commands:
        match command:
            case ('up', amount):
                aim -= amount
            case ('down', amount):
                aim += amount
            case ('forward', amount):
                xpos += amount
                depth += aim * amount

    return xpos * depth


def getCommands(input_lines):
    return [(row.split()[0], int(row.split()[1])) for row in input_lines]


if __name__ == "__main__":
    input_lines = get_lines("day2.txt")
    print(f'Solution 1 : {part1(input_lines)}')
    print(f'Solution 2 : {part2(input_lines)}')
