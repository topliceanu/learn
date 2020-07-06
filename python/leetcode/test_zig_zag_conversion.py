# -*- coding: utf-8 -*-

import unittest

from zig_zag_conversion import convert2

class TestZigZagConversion(unittest.TestCase):
    def test_convert(self):
        tests = [
            ("PAY", -1, "PAY"),
            ("PAY", 1, "PAY"),
            ("PAY", 2, "PYA"),
            ("PAYPAL", 2, "PYAAPL"),
            ("PAYPAL", 100, "PAYPAL"),
            ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
            ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
            ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
            ("ABCD", 3, "ABDC"),
        ]
        for test in tests:
            actual = convert2(test[0], test[1])
            expected = test[2]
            self.assertEqual(actual, expected, \
                'failed test={} with actual={}'.format(test, actual))
