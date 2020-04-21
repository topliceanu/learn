import unittest

from arrays_and_strings import \
    is_unique, is_unique_no_ds, \
    check_permutation, check_permutation_sort, \
    urlify, palindrome_permutation, palindrome_permutation_no_ds, \
    one_away, compression, rotate_matrix, zero_matrix

class TestArraysAndStrings(unittest.TestCase):
    def test_is_unique(self):
        tests = ['', 'a', 'abcdef', 'aa', 'abcda']
        expected = [True, True, True, False, False]
        fns = [ (lambda x : is_unique(x)), (lambda x : is_unique_no_ds(x)) ]
        for fn in fns:
            for i in range(len(tests)):
                actual = fn(tests[i])
                self.assertEqual(actual, expected[i], 'case {} for fn {} failed'.format(i, fn))

    def test_check_permutation(self):
        tests = [('', '', True), ('aaa', 'aa', False), ('abc', 'cab', True),
                ('abab', 'baba', True), ('abc', 'ab', False),
                ('ab', 'abc', False)]
        fns = [ (lambda x, y: check_permutation(x, y)),
                (lambda x, y: check_permutation_sort(x, y)) ]
        for fn in fns:
            for i in range(len(tests)):
                actual = fn(tests[i][0], tests[i][1])
                expected = tests[i][2]
                self.assertEqual(actual, expected, 'case {} for fn {} failed'.format(i, fn))

    def test_urlify(self):
        tests = [("Mr John Smith", "Mr%20John%20Smith"),
                ("  ", "%20%20"), (" a", "%20a"), ("a ", "a%20"),
                ("a  b", "a%20%20b")]

        fns = [ (lambda x: urlify(x)) ]
        for fn in fns:
            for i in range(len(tests)):
                actual = fn(tests[i][0])
                expected = tests[i][1]
                self.assertEqual(actual, expected,
                    'case {} for fn {} failed: expected={}, actual={}'.format(
                    i, fn, expected, actual))

    def test_palindrome_permutation(self):
        tests = [("Tact Coa", True), ("aba", True), ("aab", True),
                ("aaaaa", True), ('aaaaabb', True), ('aaaaabbc', False),
                ("AaBbB", True), ('Aa BbBB', True), ('', True), ('a', True)]

        fns = [ (lambda x: palindrome_permutation(x)),
                (lambda x: palindrome_permutation_no_ds(x))]
        for fni in range(len(fns)):
            fn = fns[fni]
            for i in range(len(tests)):
                actual = fn(tests[i][0])
                expected = tests[i][1]
                self.assertEqual(actual, expected,
                    'case {} for fn index {} failed: expected={}, actual={}'.format(
                    i, fni, expected, actual))

    def test_one_away(self):
        tests = [("pale", "pale", True), # Zero operations
                ("pales", "pale", True), # One insert
                ("pale", "bale", True), # One replace
                ("pale", "ple", True), # One delete
                ("pale", "paleon", False), # Two inserts
                ("pale", "pakeo", False), # One insert and one replace
                ("pale", "aleo", False), # One insert and one delete
                ("pale", "bake", False), # Two replaces
                ("pale", "bake", False), # One replace and one delete
                ("pale", "pa", False)] # Two deletes
        fns = [ (lambda x, y: one_away(x, y)) ]
        for fni in range(len(fns)):
            fn = fns[fni]
            for i in range(len(tests)):
                actual = fn(tests[i][0], tests[i][1])
                expected = tests[i][2]
                self.assertEqual(actual, expected,
                    'case {} for fn index {} failed, test={}'.format(
                    i, fni, tests[i]))

    def test_compression(self):
        tests = [('aabcccccaaa', 'a2b1c5a3'), # given test
                ('', ''), ('a', 'a'), ('ab', 'ab'), # base cases
                ('abcd', 'abcd'), ('aabb', 'aabb'), # no compression benefit
                ('aabbcc', 'aabbcc'), ('aaab', 'aaab'), # no compression benefits
                ('aaa', 'a3'), ('aaaabbb', 'a4b3'), ('aaaab', 'a4b1'),
                ('abbbb', 'a1b4')]
        fns = [ (lambda x: compression(x)) ]
        for fni in range(len(fns)):
            fn = fns[fni]
            for i in range(len(tests)):
                actual = fn(tests[i][0])
                expected = tests[i][1]
                self.assertEqual(actual, expected,
                    'case {} for fn index {} failed, test={}'.format(
                    i, fni, tests[i]))

    def test_rotate_matrix(self):
        tests = [
            ([[]], [[]]),
            ([[1]], [[1]]),
            ([[1,2],
              [4,3]],
             [[4,1],
              [3,2]]),
            ([[1,2,3],
              [8,9,4],
              [7,6,5]],
             [[7,8,1],
              [6,9,2],
              [5,4,3]]),
            ([[ 1, 2, 3, 4],
              [12,13,14, 5],
              [11,16,15, 6],
              [10, 9, 8, 7]],
             [[10,11,12, 1],
              [ 9,16,13, 2],
              [ 8,15,14, 3],
              [ 7, 6, 5, 4]]),
        ]
        for i in range(len(tests)):
            actual = rotate_matrix(tests[i][0])
            expected = tests[i][1]
            self.assertEqual(actual, expected,
                'case {} failed, test={}, actual={}'.format(
                i, tests[i], actual))

    def test_zero_matrix(self):
        tests = [
            # no zeros
            ([[1, 2],
              [3, 4]],
             [[1, 2],
              [3, 4]]),
            ([[1, 2],
              [3, 0]],
             [[1, 0],
              [0, 0]]),
            ([[0, 2],
              [3, 0]],
             [[0, 0],
              [0, 0]]),
            ([[0, 2, 3],
              [4, 0, 6],
              [7, 8, 9]],
             [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 9]]),
            ([[0, 2, 3],
              [4, 5, 6],
              [7, 8, 0]],
             [[0, 0, 0],
              [0, 5, 0],
              [0, 0, 0]]),
        ]
        for test in tests:
            expected = test[1]
            actual = zero_matrix(test[0])
            self.assertEqual(actual, expected, 'failed test={} with actual={}'
                    .format(test, actual))

        def test_string_rotation(self):
            tests = [
                ("waterbottle", "erbottlewat", True),
            ]
            for test in tests:
                expected = test[2]
                actual = is_string_rotation(test[1], test[0])
                self.assertEqual(actual, expected, 'failed test={} with actual={}'
                        .format(test, actual))
