# -*- conding: utf-8 -*-

import unittest

from spelling_suggestions import spelling_suggestions

class TestSpellingSuggestion(unittest.TestCase):
    def test_spelling_suggestions(self):
        dictionary = ['abc', 'abd', 'ace']
        suggestions = spelling_suggestions(dictionary, 'ab')
        print ">>>", suggestions
        self.assertEqual(suggestions, ['abc', 'abd'], 'should return the correct data')

        suggestions = spelling_suggestions(dictionary, 'a')
        self.assertEqual(suggestions, ['abc', 'abd', 'ace'], 'should return the correct data')
