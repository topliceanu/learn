import unittest

from src.hackerrank.bigger_is_greater import bigger_is_greater
from src.hackerrank.magic_square_forming import forming_magic_square 
from src.hackerrank.non_divisible_subset import non_divisible_subset
from src.hackerrank.queens_attack_2 import queens_attack_2
from src.hackerrank.three_d_surface_area import three_d_surface_area

class TestHackerRank(unittest.TestCase):
    def test_bigger_is_better(self):
        tests = [
            ("ab", "ba"),
            ("bb", "no answer"),
            ("hefg", "hegf"),
            ("dhck", "dhkc"),
            ("dkhc", "hcdk"),
        ]
        for (txt, expected) in tests:
            actual = bigger_is_greater(txt)
            self.assertEqual(expected, actual)

    def test_magic_square_forming(self):
        tests = [
            ([[5, 3, 4],
              [1, 5, 8],
              [6, 4, 2]],
             7),
            ([[4, 8, 2],
              [4, 5, 7],
              [6, 1, 6]],
             4),
            ([[4, 8, 2],
              [4, 5, 7],
              [6, 9, 3]],
             15),
        ]
        for test in tests:
            actual = forming_magic_square(test[0])
            expected = test[1]
            self.assertEqual(actual, expected, 'failed test={} with actual={}'.format(test, actual))

    def test_non_divisible_subset(self):
        tests = [
            ([1, 7, 2, 4], 3, 3),
            ([19, 10, 12, 10, 24, 25, 22], 4, 3),
            ([278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436], 7, 11),
        ]
        for (s, k, expected) in tests:
            actual = non_divisible_subset(s, k)
            self.assertEqual(actual, expected, 'failed s={}, k={} with actual={}'.format(s, k, actual))

    def test_queens_attack_2(self):
        tests = [
            (4, 0, 4, 4, [], 9),
            (5, 3, 4, 3, [(5,5), (4,2), (2,3)], 10),
            (1, 0, 1, 1, [], 0),
        ]
        for (n, k, r_q, c_q, obstacles, expected) in tests:
            actual = queens_attack_2(n, k, r_q, c_q, obstacles)
            self.assertEquals(expected, actual)

    def test_three_d_surface_area(self):
        tests = [
            ([[1, 3, 4],
            [2, 2, 3],
            [1, 2, 4]], 60), 
            ([[1]], 6),
        ]
        for (A, expected) in tests:
            actual = three_d_surface_area(A)
            self.assertEqual(expected, actual)