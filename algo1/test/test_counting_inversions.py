import unittest

from src.counting_inversions import sort_and_count_inversions


class TestCountingInversions(unittest.TestCase):

    def test_sort_and_count_inversions(self):
        a = [1, 3, 5, 2, 4, 6]
        (sorted_a, num_inversions) = sort_and_count_inversions(a)

        expected_a = [1, 2, 3, 4, 5, 6]
        self.assertEqual(sorted_a, expected_a, 'should have sorted the array')

        expected_num_inversions = 3
        self.assertEqual(num_inversions, expected_num_inversions)
