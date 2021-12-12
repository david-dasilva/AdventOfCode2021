import unittest
from day3 import part1, part2, epsilon
from utils.file_utils import get_lines


class TestDay3(unittest.TestCase):
    sample_input = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010'
    ]

    day_input = get_lines("day3.txt")


    def test_sample1(self):
        self.assertEqual(198, part1(self.sample_input))

    def test_epsilon(self):
        self.assertEqual(22, epsilon(self.sample_input))


if __name__ == '__main__':
    unittest.main()
