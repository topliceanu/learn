# -*- coding: utf-8 -*-

import unittest

from src.karatsuba_multiplication import multiply


class TestKaratsubaMultiplication(unittest.TestCase):

    def test_karatsuba_multiplication(self):
        x = 12
        y = 13
        self.assertEquals(multiply(x, y), x*y)

        x = 12
        y = 10
        #self.assertEquals(multiply(x, y), x*y)

        x = 5678
        y = 1234
        #self.assertEquals(multiply(x, y), x*y)
