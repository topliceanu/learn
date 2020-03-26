import unittest

from src.graph import Graph
from src.minimum_spanning_tree import prims_suboptimal_mst, prims_heap_mst, \
                              kruskal_suboptimal_mst, kruskal_union_find_mst


class TestMinimunSpanningTree(unittest.TestCase):

    def test_prims_suboptimal_mst(self):
        """ Compute minimal spanning tree given this graph:
            (a)----1----(b)
             | \         |
             4  \--3--\  2
             |         \ |
            (c)----5----(d)
        """
        g = Graph.build(edges=[('a', 'b', 1), ('a', 'c', 4), ('a', 'd', 3),
                               ('b', 'd', 2), ('c', 'd', 5)],
                        directed=False)
        expected = [('a', 'b', 1), ('a', 'c', 4), ('b', 'd', 2)]
        mst = prims_suboptimal_mst(g)
        actual = sorted(mst.get_edges())
        self.assertEqual(actual, expected, 'should have computed correct mst')

    def test_prims_suboptimal_mst_2(self):
        g = Graph.build(edges=[('a', 'b', 3), ('a', 'f', 2), ('f', 'g', 7),
                ('b', 'd', 16), ('d', 'e', 11), ('f', 'e', 1), ('g', 'e', 6),
                ('g', 'h', 15), ('e', 'h', 5), ('b', 'c', 17), ('c', 'd', 8),
                ('d', 'i', 4), ('c', 'i', 18), ('e', 'i', 10), ('h', 'i', 12),
                ('i', 'j', 9), ('h', 'j', 13)],
            directed=False)
        mst = prims_suboptimal_mst(g)
        expected = sorted([('a', 'b', 3), ('a', 'f', 2), ('e', 'f', 1),
                ('e', 'g', 6), ('e', 'h', 5), ('e', 'i', 10), ('d', 'i', 4),
                ('c', 'd', 8), ('i', 'j', 9)])
        actual = sorted(mst.get_edges())
        self.assertEqual(actual, expected, 'should compute the correct mst')

    def test_prims_heap_mst(self):
        """ Compute minimal spanning tree given this graph using
        a heap data structure.
            (a)----1----(b)
             | \         |
             4  \--3--\  2
             |         \ |
            (c)----5----(d)
        """
        g = Graph.build(edges=[('a', 'b', 1), ('a', 'c', 4), ('a', 'd', 3),
                               ('b', 'd', 2), ('c', 'd', 5)],
                        directed=False)
        expected = [('a', 'b', 1), ('a', 'c', 4), ('b', 'd', 2)]
        mst = prims_heap_mst(g)
        actual = sorted(mst.get_edges())
        self.assertEqual(actual, expected, 'should have computed correct mst')

    def test_prims_heap_mst_2(self):
        g = Graph.build(edges=[('a', 'b', 3), ('a', 'f', 2), ('f', 'g', 7),
                ('b', 'd', 16), ('d', 'e', 11), ('f', 'e', 1), ('g', 'e', 6),
                ('g', 'h', 15), ('e', 'h', 5), ('b', 'c', 17), ('c', 'd', 8),
                ('d', 'i', 4), ('c', 'i', 18), ('e', 'i', 10), ('h', 'i', 12),
                ('i', 'j', 9), ('h', 'j', 13)],
            directed=False)
        mst = prims_heap_mst(g)
        expected = sorted([('a', 'b', 3), ('a', 'f', 2), ('e', 'f', 1),
                ('e', 'g', 6), ('e', 'h', 5), ('e', 'i', 10), ('d', 'i', 4),
                ('c', 'd', 8), ('i', 'j', 9)])
        actual = sorted(mst.get_edges())
        self.assertEqual(actual, expected, 'should compute the correct mst')

    def test_kruskal_suboptimal_mst(self):
        """ Given the graph:
                (a)
                / \
               1   7
              /     \
            (b)--5--(c)
             | \     |
             4   3   6
             |     \ |
            (d)--2--(e)
        """
        g = Graph.build(edges=[('a', 'b', 1), ('a', 'c', 7), ('b', 'c', 5),
                               ('b', 'd', 4), ('d', 'e', 2), ('c', 'e', 6),
                               ('b', 'e', 3)],
                        directed=False)
        mst = kruskal_suboptimal_mst(g)
        actual = sorted(mst.get_edges())
        expected = [('a', 'b', 1), ('b', 'e', 3), ('c', 'b', 5), ('e', 'd', 2)]
        self.assertEqual(actual, expected, 'should return the correct mst')

    def test_kruskal_suboptimal_mst_2(self):
        g = Graph.build(edges=[('a', 'b', 3), ('a', 'f', 2), ('f', 'g', 7),
                ('b', 'd', 16), ('d', 'e', 11), ('f', 'e', 1), ('g', 'e', 6),
                ('g', 'h', 15), ('e', 'h', 5), ('b', 'c', 17), ('c', 'd', 8),
                ('d', 'i', 4), ('c', 'i', 18), ('e', 'i', 10), ('h', 'i', 12),
                ('i', 'j', 9), ('h', 'j', 13)],
            directed=False)
        mst = kruskal_suboptimal_mst(g)
        expected = sorted([('a', 'b', 3), ('a', 'f', 2), ('e', 'f', 1),
                ('e', 'g', 6), ('e', 'h', 5), ('e', 'i', 10), ('d', 'i', 4),
                ('c', 'd', 8), ('i', 'j', 9)])
        actual = sorted(mst.get_edges())
        self.assertEqual(actual, expected, 'should compute the correct mst')

    def test_kruskal_union_find_mst(self):
        """ Given the graph:
                (a)
                / \
               1   7
              /     \
            (b)--5--(c)
             | \     |
             4   3   6
             |     \ |
            (d)--2--(e)
        """
        g = Graph.build(edges=[('a', 'b', 1), ('a', 'c', 7), ('b', 'c', 5),
                               ('b', 'd', 4), ('d', 'e', 2), ('c', 'e', 6),
                               ('b', 'e', 3)],
                        directed=False)
        mst = kruskal_union_find_mst(g)
        actual = sorted(mst.get_edges())
        expected = [('a', 'b', 1), ('b', 'e', 3), ('c', 'b', 5), ('e', 'd', 2)]
        self.assertEqual(actual, expected, 'should return the correct mst')

    def test_kruskal_union_find_mst_2(self):
        g = Graph.build(edges=[('a', 'b', 3), ('a', 'f', 2), ('f', 'g', 7),
                ('b', 'd', 16), ('d', 'e', 11), ('f', 'e', 1), ('g', 'e', 6),
                ('g', 'h', 15), ('e', 'h', 5), ('b', 'c', 17), ('c', 'd', 8),
                ('d', 'i', 4), ('c', 'i', 18), ('e', 'i', 10), ('h', 'i', 12),
                ('i', 'j', 9), ('h', 'j', 13)],
            directed=False)
        mst = kruskal_union_find_mst(g)
        expected = sorted([('a', 'b', 3), ('a', 'f', 2), ('e', 'f', 1),
                ('e', 'g', 6), ('e', 'h', 5), ('e', 'i', 10), ('d', 'i', 4),
                ('c', 'd', 8), ('i', 'j', 9)])
        actual = sorted(mst.get_edges())
        self.assertEqual(actual, expected, 'should compute the correct mst')
