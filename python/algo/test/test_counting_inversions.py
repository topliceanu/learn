# -*- coding: utf-8 -*-

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

    def test_count_inversions_for_a_smaller_set(self):
        a = [3, 2, 1, 6, 5, 4]
        (sorted_a, num_inversions) = sort_and_count_inversions(a)

        expected_a = [1, 2, 3, 4, 5, 6]
        self.assertEqual(sorted_a, expected_a, 'should have sorted the array')

        expected_num_inversions = 6
        self.assertEqual(num_inversions, expected_num_inversions)

    def test_count_inversions_when_right_array_contains_last_data(self):
        a = [1,2,5,6,3,4,7,8]
        (sorted_a, num_inversions) = sort_and_count_inversions(a)

        expected_a = [1,2,3,4,5,6,7,8]
        self.assertEqual(sorted_a, expected_a, 'should have sorted the array')

        expected_num_inversions = 4
        self.assertEqual(num_inversions, expected_num_inversions)

    def test_count_inversions_when_left_array_contains_last_data(self):
        a = [1,2,7,8,3,4,5,6]
        (sorted_a, num_inversions) = sort_and_count_inversions(a)

        expected_a = [1,2,3,4,5,6,7,8]
        self.assertEqual(sorted_a, expected_a, 'should have sorted the array')

        expected_num_inversions = 8
        self.assertEqual(num_inversions, expected_num_inversions)

    def test_count_inversions_from_online_test_case(self):
        a = [1, 6, 3, 5, 2, 100, 34, 23, 11, 9]
        (_, num_inversions) = sort_and_count_inversions(a)
        self.assertEqual(num_inversions, 15)

    def test_count_inversions_from_another_online_test_case(self):
        a = [1,3,5,2,4,12,11]
        (_, num_inversions) = sort_and_count_inversions(a)
        self.assertEqual(num_inversions, 4)
