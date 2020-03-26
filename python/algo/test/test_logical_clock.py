# -*- coding: utf-8 -*-

import unittest

from src.logical_clock import LamportClock, VectorClock


class TestLogicalClock(unittest.TestCase):

    def test_lamport_clock(self):
        lc1 = LamportClock()
        lc2 = LamportClock()

        lc1.increment()
        lc1.increment()
        lc2.increment()

        lc2.merge(lc1)

        self.assertEqual(lc1.read(), 2, 'after two increments should be 2')
        self.assertEqual(lc2.read(), 3, 'should now be larger than lc1')

    def test_update_vector_clock_for_multiple_processes(self):
        """ This test emulates http://en.wikipedia.org/wiki/File:Vector_Clock.svg"""
        a = VectorClock('a')
        b = VectorClock('b')
        c = VectorClock('c')

        # c sends message to b.
        c.increment()

        # b received message from c.
        b.update(c.read())
        self.assertEqual(set(b.read().iteritems()), set({'b': 1, 'c': 1}.iteritems()),
            'b after receiving a message from c')

        # b sends message to a.
        b.increment()

        # a receives message from b.
        a.update(b.read())
        self.assertEqual(set(a.read().iteritems()), set({'a': 1, 'b': 2, 'c': 1}.iteritems()),
            'a after receiving message from b')

        # a sends message to b.
        a.increment()

        # b sends message to c.
        b.increment()

        # c receives message from b.
        c.update(b.read())
        self.assertEqual(set(c.read().iteritems()), set({'b': 3, 'c': 2}.iteritems()),
            'a after receiving message from b')

        # b receives message from a.
        b.update(a.read())
        self.assertEqual(set(b.read().iteritems()), set({'a': 2, 'b': 4, 'c': 1}.iteritems()),
            'a after receiving message from b')

        # c sends message to a.
        c.increment()

        # a receives message from c.
        a.update(c.read())
        self.assertEqual(set(a.read().iteritems()), set({'a': 3, 'b': 3, 'c': 3}.iteritems()),
            'a after receiving message from c')

        # b sends message to c.
        b.increment()

        # c receives message from b.
        c.update(b.read())
        self.assertEqual(set(c.read().iteritems()), set({'a': 2, 'b': 5, 'c': 4}.iteritems()),
            'c after receiving message from b')

        # c sends message to a.
        c.increment()

        # a receives message from c.
        a.update(c.read())
        self.assertEqual(set(a.read().iteritems()), set({'a': 4, 'b': 5, 'c': 5}.iteritems()),
            'a after receiving message from c')

    def test_compare_vector_clocks(self):
        """ This test emulates http://en.wikipedia.org/wiki/File:Vector_Clock.svg"""
        a = VectorClock('a')
        b = VectorClock('b')
        c = VectorClock('c')

        # c sends message to b.
        c.increment()
        vc1 = c.read()
        # b received message from c.
        b.update(c.read())
        vc3 = b.read()
        # b sends message to a.
        b.increment()
        # a receives message from b.
        a.update(b.read())
        # a sends message to b.
        a.increment()
        # b sends message to c.
        b.increment()
        vc4 = b.read()
        # c receives message from b.
        c.update(b.read())
        # b receives message from a.
        b.update(a.read())
        # c sends message to a.
        c.increment()
        # a receives message from c.
        a.update(c.read())
        vc5 = a.read()
        # b sends message to c.
        b.increment()
        vc6 = b.read()
        # c receives message from b.
        c.update(b.read())
        # c sends message to a.
        c.increment()
        # a receives message from c.
        a.update(c.read())
        vc2 = a.read()

        self.assertLess(vc1, vc2, 'initial message from c to b and last message from c to a')
        self.assertLess(vc3, vc4, 'b receives from c and send back to c')
        self.assertLess(vc5, vc2, 'a receives two messages from c')
        self.assertLess(vc4, vc6, 'b sends two message to c one before and one after receiving from a')
