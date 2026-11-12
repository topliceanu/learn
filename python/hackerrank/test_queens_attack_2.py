import unittest

from queens_attack_2 import queens_attack_2

class TestQueensAttack2(unittest.TestCase):
    def test_queens_attack_2(self):
        tests = [
            (4, 0, 4, 4, [], 9),
            (5, 3, 4, 3, [(5,5), (4,2), (2,3)], 10),
            (1, 0, 1, 1, [], 0),
        ]
        for (n, k, r_q, c_q, obstacles, expected) in tests:
            actual = queens_attack_2(n, k, r_q, c_q, obstacles)
            self.assertEquals(expected, actual)