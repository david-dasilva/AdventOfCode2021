import unittest
from day2 import part1, part2
from utils.file_utils import get_lines


class TestDay2(unittest.TestCase):
    sample_input = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2"
    ]

    day_input = get_lines("day2.txt")

    def test_sample1(self):
        self.assertEqual(150, part1(self.sample_input))

    def test_sample2(self):
        self.assertEqual(900, part2(self.sample_input))

    def test_part1(self):
        self.assertEqual(1580000, part1(self.day_input))

    def test_part2(self):
        self.assertEqual(1251263225, part2(self.day_input))


if __name__ == '__main__':
    unittest.main()
