# -*- coding: utf-8 -*-

import unittest

from src.graph import Graph
from src.maximum_flow import ford_fulkerson_maximum_flow


class TestMaximumFlow(unittest.TestCase):

    def test_ford_fulkerson_maximum_flow_1(self):
        """ Given the graph:
          /--1->(a)--1---\v
        (s)      v1      (t)
          \--1->(b)--1---/^
        """
        g = Graph.build(edges=[('s', 'a', 1), ('s', 'b', 1),
                ('a', 'b', 1), ('a', 't', 1), ('b', 't', 1)],
            directed=True)
        (max_flow, flow) = ford_fulkerson_maximum_flow(g, 's', 't')
        expected_max_flow = 2
        expected_flow_edges = [('a', 'b', 0), ('a', 't', 1), ('s', 'a', 1),
                               ('s', 'b', 1), ('b', 't', 1)]
        self.assertEqual(max_flow, expected_max_flow, 'should compute max flow')
        self.assertListEqual(flow.get_edges(), expected_flow_edges,
            'should compute flow through edges correctly')

    def x_test_ford_fulkerson_maximum_flow_2(self):
        # TODO fix this!
        """ Given the graph:
          16/-->(a)--12-->(b)---\20
          /     | ^      / ^     \v
        (s)    9| |4 /-9/  |7    (t)
          \     v | v      |     /^
         13\--->(c)--14-->(d)---/4
        """
        g = Graph.build(edges=[('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 9),
                ('c', 'a', 4), ('a', 'b', 12), ('c', 'd', 14), ('b', 'c', 9),
                ('d', 'b', 7), ('b', 't', 20), ('d', 't', 4)],
            directed=True)
        (max_flow, flow) = ford_fulkerson_maximum_flow(g, 's', 't')
        expected_max_flow = 23
        self.assertEqual(max_flow, expected_max_flow, 'should compute max flow')

    def test_ford_fulkerson_maximum_flow_3(self):
        """ Given the graph:
           /-5->(b)--6-->(e)-6-\
          /        \    /^      \v
        (s)        3\__/3       (t)
          \        /    \v      /^
           \-5->(c)--1-->(f)-6-/
        """
        g = Graph.build(edges=[('s', 'b', 5), ('s', 'c', 5), ('b', 'e', 6),
                ('c', 'f', 1), ('b', 'f', 3), ('c', 'e', 3), ('e', 't', 6),
                ('f', 't', 6)],
            directed=True)
        (max_flow, flow) = ford_fulkerson_maximum_flow(g, 's', 't')
        expected_max_flow = 9
        expected_flow_edges = [('c', 'e', 3), ('c', 'f', 1),
                ('b', 'e', 3), ('b', 'f', 2), ('e', 't', 6),
                ('f', 't', 3), ('s', 'c', 4), ('s', 'b', 5)]
        self.assertEqual(max_flow, expected_max_flow, 'should compute max flow')
        self.assertListEqual(flow.get_edges(), expected_flow_edges,
            'should compute flow through edges correctly')

    def test_ford_fulkerson_maximum_flow_4(self):
        """ Given the graph:
           3/-->(o)--3-->(q)---\2
          /      |        |     \v
        (s)     2|        |4    (t)
          \      v        v     /^
          3\--->(p)--2-->(r)---/3
        """
        g = Graph.build(edges=[('s', 'o', 3), ('s', 'p', 3), ('o', 'p', 2),
                ('o', 'q', 3), ('p', 'r', 2), ('q', 'r', 4), ('q', 't', 2),
                ('r', 't', 3)],
            directed=True)
        (max_flow, flow) = ford_fulkerson_maximum_flow(g, 's', 't')
        expected_max_flow = 5
        expected_flow_edges = [('o', 'q', 3), ('o', 'p', -1),
                ('q', 'r', 1), ('q', 't', 2), ('p', 'r', 2),
                ('s', 'p', 3), ('s', 'o', 2), ('r', 't', 3)]
        self.assertEqual(max_flow, expected_max_flow, 'should compute max flow')
        self.assertListEqual(flow.get_edges(), expected_flow_edges,
            'should compute flow through edges correctly')

    def test_ford_fulkerson_maximum_flow_5(self):
        """ Given the graph:

