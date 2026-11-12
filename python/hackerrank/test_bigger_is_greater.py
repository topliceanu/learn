import unittest

from bigger_is_greater import bigger_is_greater 

class TestBiggerIsGreater(unittest.TestCase):
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
