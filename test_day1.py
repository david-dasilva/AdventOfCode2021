import unittest
from day1 import part1, part2
from utils.file_utils import get_lines


class Test(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
