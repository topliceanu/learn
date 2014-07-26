import unittest

from src.randomized_selection import randomized_selection


class RandomizedSelection(unittest.TestCase):

    def test_randomized_selection(self):
        arr = [10, 8, 2, 4]
        actual = randomized_selection(arr, len(arr), 2)
        expected = 8
        self.assertEqual(actual, expected, 'should select the third position')
