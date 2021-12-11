from utils.file_utils import get_lines


def part1(input):
    xpos = 0
    depth = 0

    for command in input:
        cmd = getDirection(command)
        amount = getAmount(command)
        if cmd == "up":
            depth -= amount
        elif cmd == "down":
            depth += amount
        else:
            xpos += amount

    return xpos * depth


def part2(input):
    xpos = 0
    depth = 0
    aim = 0
    for command in input:
        cmd = getDirection(command)
        amount = getAmount(command)
        if cmd == "up":
            aim -= amount
        elif cmd == "down":
            aim += amount
        else:
            xpos += amount
            depth += aim * amount

    return xpos * depth


def getDirection(command: str):
    return command.split(" ")[0]


def getAmount(command: str):
    return int(command.split(" ")[1])


if __name__ == "__main__":
    input_list = get_lines("day2.txt")
    print(f'Solution 1 : {part1(input_list)}')
    print(f'Solution 2 : {part2(input_list)}')
