# -*- coding: utf-8 -*-

import unittest

from src.reverse_polish_notation import reverse_polish_notation


class TestReversePolishNotation(unittest.TestCase):

  def test_simple_case(self):
    expression = "1 + 2".split()
    expected = "1 2 +".split()
    actual = reverse_polish_notation(expression)
    self.assertEqual(actual, expected)

  def test_simple_case_2(self):
    expression = "1 + 2 - 3".split()
    expected = "1 2 + 3 -".split()
    actual = reverse_polish_notation(expression)
    self.assertEqual(actual, expected)

  def test_no_paranthesis(self):
    expression = "3 - 4 * 5".split()
    expected = "3 4 5 * -".split()
    actual = reverse_polish_notation(expression)
    self.assertEqual(actual, expected)

  def test_simple_paranthesis(self):
    expression = "( 3 - 4 ) * 5".split()
    expected = "3 4 - 5 *".split()
    actual = reverse_polish_notation(expression)
    self.assertEqual(actual, expected)

  #def test_complicated_expression(self):
  #  expression = "5 + ((1 + 2) * 4) − 3".split()
  #  expected = "5 1 2 + 4 * + 3 -".split()
  #  actual = reverse_polish_notation(expression)
  #  self.assertEqual(actual, expected)

  def test_even_more_complicated_expression(self):
    expression = "3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3".split()
    expected = "3 4 2 * 1 5 - 2 3 ^ ^ / +".split()
    actual = reverse_polish_notation(expression)
    self.assertEqual(actual, expected)

  #def test_expression_with_functions(self):
  #  expression = "sin ( max ( 2 , 3 ) / 3 * 3 )".split()
  #  expected = "2 3 max 3 / 3 * sin".split()
  #  actual = reverse_polish_notation(expression)
  #  self.assertEqual(actual, expected)
