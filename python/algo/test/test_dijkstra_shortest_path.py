import unittest

from src.graph import Graph
from src.dijkstra_shortest_path import get_frontier, pick_min_path, \
                                   shortest_path_naive, shortest_path_heap, \
                                   VISITED, NOT_VISITED


class TestDijkstraShortestPath(unittest.TestCase):

    def test_shortest_path_heap(self):
        """ Compute a shortest path using a naive implementation.
        Given the following graph:

            (s)---1-->(v)
             |        /|
             4  /-2--/ 6
             V v      \V
            (w)---3-->(t)
        """
        g = Graph.build(edges=[('s', 'v', 1), ('s', 'w', 4), ('v', 'w', 2),
                               ('v', 't', 6), ('w', 't', 3)],
                        directed=True)
        length_to = shortest_path_heap(g, 's')
        self.assertEqual(length_to['s'], 0, 'shortest path to self is 0')
        self.assertEqual(length_to['v'], 1)
        self.assertEqual(length_to['w'], 3)
        self.assertEqual(length_to['t'], 6)

    def test_shortest_path_heap_case1(self):
        """ Compute a shortest path using the heap implementation. """
        g = Graph.build(edges=[
            ('a','c',3),('c','b',10),('a','b',15),('d','b',9),
            ('a','d',4),('d','f',7),('d','e',3),('e','g',1),
            ('e','f',5),('g','f',2),('f','b',1)],
            directed=True)

        shortest_path = shortest_path_heap(g, 'a')
        self.assertEqual(shortest_path['g'], 8)
        self.assertEqual(shortest_path['b'], 11)

    def test_shortest_path_heap_case2(self):
        """ Compute a shortest path using the heap implementation. """
        g = Graph.build(edges=[
            ('a','b',2),('a','c',2),('a','d',4),('a','e',2),
            ('a','f',4),('b','g',5),('c','d',4),('e','d',1)],
            directed=True)

        shortest_path = shortest_path_heap(g, 'a')
        self.assertEqual(shortest_path['d'], 3)

    def test_shortest_path_heap_case3(self):
        """ Compute a shortest path using the heap implementation. """
        g = Graph.build(edges=[
            ('a','b',1),('a','c',4),('a','d',4),('b','c',1),('c','d',1)],
            directed=True)

        shortest_path = shortest_path_heap(g, 'a')
        self.assertEqual(shortest_path['d'], 3)

    def test_shortest_path_naive(self):
        """ Compute a shortest path using a naive implementation.
        Given the following graph:

            (s)---1-->(v)
             |        /|
             4  /-2--/ 6
             V v      \V
            (w)---3-->(t)
        """
        g = Graph.build(edges=[('s', 'v', 1), ('s', 'w', 4), ('v', 'w', 2),
                               ('v', 't', 6), ('w', 't', 3)],
                        directed=True)
        length_to = shortest_path_naive(g, 's')
        self.assertEqual(length_to['s'], 0, 'shortest path to self is 0')
        self.assertEqual(length_to['v'], 1)
        self.assertEqual(length_to['w'], 3)
        self.assertEqual(length_to['t'], 6)

    def test_shortest_path_naive_case1(self):
        """ Compute a shortest path using the heap implementation. """
        g = Graph.build(edges=[
            ('a','c',3),('c','b',10),('a','b',15),('d','b',9),
            ('a','d',4),('d','f',7),('d','e',3),('e','g',1),
            ('e','f',5),('g','f',2),('f','b',1)],
            directed=True)

        shortest_path = shortest_path_naive(g, 'a')
        self.assertEqual(shortest_path['g'], 8)
        self.assertEqual(shortest_path['b'], 11)

    def test_shortest_path_naive_case2(self):
        """ Compute a shortest path using the heap implementation. """
        g = Graph.build(edges=[
            ('a','b',2),('a','c',2),('a','d',4),('a','e',2),
            ('a','f',4),('b','g',5),('c','d',4),('e','d',1)],
            directed=True)

        shortest_path = shortest_path_naive(g, 'a')
        self.assertEqual(shortest_path['d'], 3)

    def test_shortest_path_naive_case3(self):
        """ Compute a shortest path using the heap implementation. """
        g = Graph.build(edges=[
            ('a','b',1),('a','c',4),('a','d',4),('b','c',1),('c','d',1)],
            directed=True)

        shortest_path = shortest_path_naive(g, 'a')
        self.assertEqual(shortest_path['d'], 3)


    def test_get_frontier(self):
        """ Makes sure frontier edges are correctly picked.
            (1)--->(2)
             |      |
             V      V
            (3)<---(4)
        """
        g = Graph.build(edges=[(1,2), (1,3), (2,4), (4,3)], directed=True)
        explored_vertices = [1,3]

        actual = get_frontier(g, explored_vertices)
        expected = set([(1,2,True)])
        self.assertEqual(actual, expected, 'should only return the only node ' \
                                      'reachable that has not yet been visited')
