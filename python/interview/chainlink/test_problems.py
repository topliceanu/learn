import unittest

from problems import solution, encryptionValidity, calculate, tokenize, calculate_two

class TestProblem(unittest.TestCase):
    def test_problem(self):
        tests = [
            ([2, 5, 1, 4], 8),
            ([4, 5], 5),
            ([6, 8, 3, 4, 2, 5], 12),
            ([1, 1, 1], 1),
            ([], 0),
            ([1, 2, 3, 4, 5], 11),
            ([5, 4, 3, 2, 1], 5),
            ([4, 4, 9, 2, 3], 10),
        ]
        for test in tests:
            actual = solution(test[0])
            expected = test[1]
            self.assertEqual(actual, expected, 'test={} failed with actual={}'.format(test, actual))

    def test_encryptionValidity(self):
        tests = [
            (1000, 10000, [2, 4, 8, 2], 1, 400000),
            (100, 1000, [2, 4], 0, 200000),
            (100, 1000, [2, 2, 4, 4, 4], 0, 500000),
            (9677958, 50058356, [83315, 22089, 19068, 64911, 67636, 4640, 80192, 98971], 1, 100000)
        ]
        for test in tests:
            actual = encryptionValidity(test[0], test[1], test[2])
            expected = (test[3], test[4])
            self.assertEqual(actual, expected, 'test={} failed with actual={}'.format(test, actual))

    def test_tokenize(self):
        tests = [
            ('1 + 2 - 3', [1, '+', 2, '-', 3]),
            ('  1  +   2 -    3   ', [1, '+', 2, '-', 3]),
            ('1+2-3', [1, '+', 2, '-', 3]),
            ('1+(2-3)', [1, '+', '(', 2, '-', 3, ')']),
            ('1+ (2- (3 + 4) - 5)', [1, '+', '(', 2, '-', '(', 3, '+', 4, ')', '-', 5, ')']),
            ('100 + 1000', [100, '+', 1000])
        ]
        for test in tests:
            actual = tokenize(test[0])
            expected = test[1]
            self.assertEqual(actual, expected, 'test={} failed with actual={}'.format(test, actual))

    def test_calculate_two(self):
        tests = [
            ('1 + 2 - 3', 0),
            ('1 - (2 + 3)', -4),
            ('1+ (2- (3 + 4) - 5)', -9),
            ('100 + 1000', 1100),
            ('1 - (2 - 3)', 2),
        ]
        for test in tests:
            actual = calculate_two(test[0])
            expected = test[1]
            self.assertEqual(actual, expected, 'test={} failed with actual={}'.format(test, actual))
