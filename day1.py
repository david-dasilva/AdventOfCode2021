from utils.file_utils import get_lines
from unittest import TestCase


def part1(depths):
    x, y = depths[:-1], depths[1:]
    result = sum(1 for xs, ys in zip(x, y) if ys > xs)

    return result


def part2(depths):
    increases = 0
    previous_window = 0
    max_index = len(depths)
    current_index = 0
    while current_index + 2 < max_index:
        current_window = depths[current_index] + depths[current_index + 1] + depths[current_index + 2]
        if 0 < previous_window < current_window:
            increases += 1
        previous_window = current_window
        current_index += 1
    return increases


if __name__ == "__main__":
    input_list = [int(depth) for depth in get_lines("day1.txt")]
    print(f'Solution 1 : {part1(input_list)}')
    print(f'Solution 2 : {part2(input_list)}')


class Test(TestCase):
    sample_input = [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263
    ]

    day_input = [int(depth) for depth in get_lines("day1.txt")]

    def test_sample1(self):
        self.assertEqual(7, part1(self.sample_input))

    def test_sample2(self):
        self.assertEqual(5, part2(self.sample_input))

    def test_part1(self):
        self.assertEqual(1139, part1(self.day_input))

    def test_part2(self):
        self.assertEqual(1103, part2(self.day_input))
