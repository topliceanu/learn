# -*- coding: utf-8 -*-

import unittest

from integer_to_roman import integer_to_roman

class TestIntegerToRoman(unittest.TestCase):
    def test_integer_to_roman(self):
        tests = [
            (0, ''),
            (1, 'I'),
            (3, 'III'),
            (4, 'IV'),
            (5, 'V'),
            (6, 'VI'),
            (9, 'IX'),
            (10, 'X'),
            (11, 'XI'),
            (40, 'XL'),
            (49, 'XLIX'),
            (58, 'LVIII'),
            (87, 'LXXXVII'),
            (92, 'XCII'),
            (101, 'CI'),
            (469, 'CDLXIX'),
            (943, 'CMXLIII'),
            (6666, 'NMDCLXVI'),
        ]
        for test in tests:
            actual = integer_to_roman(test[0])
            expected = test[1]
            self.assertIn(actual, expected, \
                'failed test={} with actual={}'.format(test, actual))

