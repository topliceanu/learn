import unittest

from src.match_parantheses import match_parantheses


class MatchParantheses(unittest.TestCase):

    def test_match_parantheses(self):
        s = ''
        actual = match_parantheses(s)
        self.assertTrue(actual, 'empty string respects the rule of '+
                                  'parantheses opening and closing')

        s = '[]()[]()'
        actual = match_parantheses(s)
        self.assertTrue(actual, 'independent parantheses work')

        s = '1[2]3(4)5[6]7(8)'
        actual = match_parantheses(s)
        self.assertTrue(actual, 'parantheses mixed with data work')

        s = '[[[(())]]]'
        actual = match_parantheses(s)
        self.assertTrue(actual, 'nested parantheses work')

        s = '[()[[))([])'
        actual = match_parantheses(s)
        self.assertFalse(actual, 'not matching')

        s = '[a()sd[f[)asd)(f[g])a]'
        actual = match_parantheses(s)
        self.assertFalse(actual, 'not matching even if mixed with data')
