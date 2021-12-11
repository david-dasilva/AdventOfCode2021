from utils.file_utils import get_lines
from itertools import pairwise


def part1(depths):
    x, y = depths[:-1], depths[1:]
    result = sum(1 for xs, ys in zip(x, y) if ys > xs)

    return result


def part2(depths):
    x, y = triplewise(depths[:-1]), triplewise(depths[1:])
    result = sum(1 for xs, ys in zip(x, y) if sum(ys) > sum(xs))
    return result


def triplewise(iterable):
    for (a, _), (b, c) in pairwise(pairwise(iterable)):
        yield a, b, c


if __name__ == "__main__":
    input_list = [int(depth) for depth in get_lines("day1.txt")]
    print(f'Solution 1 : {part1(input_list)}')
    print(f'Solution 2 : {part2(input_list)}')


