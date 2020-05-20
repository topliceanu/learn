import unittest

from magic_square_forming import formingMagicSquare

class TestMagicSquareForming(unittest.TestCase):
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
            actual = formingMagicSquare(test[0])
            expected = test[1]
            self.assertEqual(actual, expected, 'failed test={} with actual={}'.format(test, actual))
