# -*- coding: utf-8 -*-

import unittest

from src.graph import Graph


class TestGraph(unittest.TestCase):

    def test_split_edge_with_value(self):
        edge = (1,2,3)
        g = Graph()
        (tail, head, value) = g.split_edge(edge)

        self.assertEqual(tail, 1)
        self.assertEqual(head, 2)
        self.assertEqual(value, 3)

    def test_split_edge_without_value(self):
        edge = (1,2)
        g = Graph()
        (tail, head, value) = g.split_edge(edge)

        self.assertEqual(tail, 1)
        self.assertEqual(head, 2)
        self.assertEqual(value, True)

    def test_add_vertex(self):
        g = Graph()
        g.add_vertex(1)

        self.assertIn(1, g.table, 'should have stored a key in the hash')
        self.assertEqual(g.table[1], {}, 'should have stored an empty hash')

    def test_add_edge_multiple_times_nothing_happens(self):
        g = Graph(True)
        g.add_edge((1,2,3))
        g.add_edge((1,2,3))
        g.add_edge((1,2,3))
        g.add_edge((1,2,3))

        self.assertIn(1, g.table, 'should have stored the tail in table')
        self.assertIn(2, g.table[1], 'should have stored the head in table')

    def test_add_edge_for_undirected_graph(self):
        g = Graph(False)
        g.add_edge((1,2,3))

        self.assertIn(1, g.table, 'should have stored a key for tail vertex')
        self.assertIn(2, g.table[1], 'should have stored the edge')
        self.assertEqual(g.table[1][2], 3, 'should have stored the edge value')

        self.assertIn(2, g.table, 'should have stored a key for head vertex')
        self.assertIn(1, g.table[2], 'should have stored the reversed edge')
        self.assertEqual(g.table[2][1], 3, 'should have stored the edge value')

    def test_add_edge_for_directed_graph(self):
        g = Graph(True)
        g.add_edge((1,2,3))

        self.assertIn(1, g.table, 'should have stored a key for tail vertex')
        self.assertIn(2, g.table[1], 'should have stored the edge')
        self.assertEqual(g.table[1][2], 3, 'should have stored the edge value')

        self.assertIn(2, g.table, 'should not have stored the node')
        self.assertNotIn(1, g.table[2], 'should not have stored the reverse edge')

    def test_add_edge_does_not_add_self_edges(self):
        g = Graph(True)
        g.add_edge((1,2))
        g.add_edge((1,1))

        self.assertNotIn(1, g.table[1], 'should not have added a self edge')

    def test_get_vertices_for_directed_graph(self):
        g = Graph(True)
        g.add_edge((1,2))

        actual = g.get_vertices()
        expected = [1,2]
        self.assertEqual(actual, expected, 'should return all vertices')

    def test_get_vertices_for_undirected_graph(self):
        g = Graph(False)
        g.add_edge((1,2))
        g.add_edge((2,3))
        g.add_edge((3,1))

        actual = g.get_edges()
        expected = [(1,2,True), (1,3,True), (2,3,True)]

        self.assertEqual(actual, expected, 'should return only one way edges')

    def test_adjacent_in_directed_graphs(self):
        g = Graph(True)
        g.add_edge((1,2))

        self.assertTrue(g.adjacent(1,2), 'should find them adjacent')
        self.assertFalse(g.adjacent(2,1), 'the edge is pointing the other way')

    def test_adjacent_in_undirected_graphs(self):
        g = Graph(False)
        g.add_edge((1,2))

        self.assertTrue(g.adjacent(1,2), 'should find them adjacent')
        self.assertTrue(g.adjacent(2,1), 'un-directed graph')

    def test_neighbours_in_directed_graph(self):
        g = Graph(True)
        g.add_edge((1,2))
        g.add_edge((1,3))

        expected = [2, 3]
        actual = g.neighbours(1)
        self.assertEqual(actual, expected, 'should find neighbours of 1')

        expected = []
        actual = g.neighbours(2)
        self.assertEqual(actual, expected, '2 has no neighbours')

    def test_incident_in_directed_graph(self):
        g = Graph(directed = True)
        g.add_edge((2,1))
        g.add_edge((3,1))

        actual = g.incident(1)
        expected = [2, 3]
        self.assertEqual(actual, expected, '1 has two incident vertexes')

    def test_incident_in_undirected_graph(self):
        g = Graph(directed = False)
        g.add_edge((2,1))
        g.add_edge((3,1))

        actual = g.incident(1)
        expected = [2, 3]
        self.assertEqual(actual, expected, '1 has two incident vertexes')

        incident = g.incident(1)
        neighbours = g.neighbours(1)
        self.assertEqual(incident, neighbours,
                'should be the same for undirected graphs')

    def test_incident_invariant_is_preserved_throughout_graph_operations(self):
        g = Graph(directed = True)

        g.add_vertex(1)
        self.assertEqual(g.incident(1), [],
            'should have instantiated an empty set of ingress vertices')

        g.add_edge((2,1))
        g.add_edge((2,1))
        self.assertEqual(g.incident(1), [2],
            'set of incident vertices is preserved')
        self.assertEqual(g.incident(2), [], 'no vertices incident in 2')

        g.remove_edge((2,1))
        self.assertEqual(g.incident(1), [],
            '2 was removed from the list of incident vertices for 3')

    def test_incident_vertices_are_correctly_maintained_after_remove_vertex(self):
        g = Graph(directed=True)
        g.add_edge((1,2))
        g.add_edge((2,3))
        g.add_edge((3,1))
        # table: {1: {2: True}, 2: {3: True}, 3: {1: True}}
        # incident: {1: set([3]), 2: set([1]), 3: set([2])}
        g.remove_vertex(1)
        self.assertEqual(g.table, {2: {3: True}, 3: {}})
        self.assertEqual(g.incident_vertices, {2: set(), 3: set([2])})

        g = Graph(directed=False)
        g.add_edge((1,2))
        g.add_edge((2,3))
        g.add_edge((3,1))
        # table: {1: {2: True, 3: True}, 2: {1: True, 3: True}, 3: {1: True, 2: True}}
        # incident: {1: set([2, 3]), 2: set([1, 3]), 3: set([1, 2])}
        g.remove_vertex(1)
        self.assertEqual(g.table, {2: {3: True}, 3: {2: True}})
        self.assertEqual(g.incident_vertices, {2: set([3]), 3: set([2])})

    def test_get_edge_value_in_directed_graph(self):
        g = Graph(True)
        g.add_edge((1,2,3))

        self.assertEqual(g.get_edge_value((1,2)), 3,
                'should have stored value')
        self.assertIsNone(g.get_edge_value((2,1)),
                'should have no value for reverse edge')

    def test_set_edge_value_if_edge_exists(self):
        g = Graph(True)
        g.add_edge((1,2,10))
        g.set_edge_value((1,2), 20)

        self.assertEqual(g.table[1][2], 20,
                'should have updated the edge value')

    def test_set_edge_value_if_graph_is_directed_and_inverse_edge_exists(self):
        g = Graph(True)
        g.add_edge((1,2,10))
        g.add_edge((2,1,20))
        g.set_edge_value((1,2), 30)

        self.assertEqual(g.table[1][2], 30, 'has updated the edge')
        self.assertEqual(g.table[2][1], 20, 'reverse edge remained the same')

    def test_set_edge_value_works_for_undirected_graphs(self):
        g = Graph(False)
        g.add_edge((1,2,10))
        g.set_edge_value((1,2), 30)

        self.assertEqual(g.table[1][2], 30, 'has updated the edge')
        self.assertEqual(g.table[2][1], 30, 'reverse edge was updated too')

    def test_remove_edge_in_directed_graph(self):
        g = Graph(True)
        g.add_edge((1,2,10))
        g.add_edge((2,3,11))
        g.add_edge((3,1,12))

        g.remove_edge((2,3))
        self.assertEqual(g.table[1][2], 10, 'should have kept the edge')
        self.assertEqual(g.table[3][1], 12, 'should have kept the edge')
        self.assertEqual(g.table[2], {}, 'should have removed the edge')

    def test_remove_edge_in_undirected_graph(self):
        g = Graph(False)
        g.add_edge((1,2,10))
        g.add_edge((2,3,11))
        g.add_edge((3,1,12))

        g.remove_edge((2,3))

        self.assertEqual(g.table[1][2], 10, 'no removals')
        self.assertEqual(g.table[1][3], 12, 'no removals')
        self.assertEqual(g.table[2][1], 10, 'removed the edge from tail')
        self.assertEqual(g.table[3][1], 12, 'removed the edge from head')

    def test_remove_vertex(self):
        g = Graph(False)
        g.add_edge((1,2))
        g.add_edge((2,3))
        g.add_edge((3,1))

        g.remove_vertex(3)

        self.assertTrue(g.table[1][2], 'should keep edges not involving 3')
        self.assertTrue(g.table[2][1], 'should keep edges not involving 3')
        self.assertNotIn(3, g.table, 'vertex 3 disappeared')
        self.assertNotIn(3, g.table[1], 'edge from 3 to 1 dissappeared')

    def test_remove_vertex_removes_value_as_well(self):
        g = Graph(False)
        g.add_vertex(1)
        g.set_vertex_value(1, 100)
        g.remove_vertex(1)
        self.assertIsNone(g.get_vertex_value(1), '1 is no longer in the graph')

    def test_rename_vertex(self):
        g = Graph(True)
        g.add_edge((1,2))
        g.add_edge((2,3))
        g.add_edge((3,4))
        g.add_edge((4,1))
        g.rename_vertex(3,3.5)

        self.assertNotIn(3, g.table, 'removed vertex 3')
        self.assertNotIn(3, g.table[2], 'removed vertex (2,3)')

        self.assertIn(3.5, g.table, 'add vertex 3.5')
        self.assertIn(4, g.table[3.5], '3.5 tails to 4')

    def test_rename_vertex_should_remove_self_edges(self):
        g = Graph(True)
        g.add_edge((1,2))
        g.add_edge((2,3))
        g.add_edge((3,4))
        g.add_edge((4,1))
        g.rename_vertex(2,1)

        self.assertTrue(g.table[1][3])
        self.assertTrue(g.table[3][4])
        self.assertTrue(g.table[4][1])
        self.assertNotIn(2, g.table[1])
        self.assertNotIn(2, g.table)

    def test_ingress(self):
        g = Graph(False)
        g.add_edge((1, 2, 10))
        g.add_edge((1, 3, 11))
        g.add_edge((2, 3, 12))

        actual = g.ingress(1)
        expected = [(2, 1, 10), (3, 1, 11)]
        self.assertEqual(actual, expected, 'should return ingress edges')

    def test_egress(self):
        g = Graph(False)
        g.add_edge((1, 2, 10))
        g.add_edge((1, 3, 11))
        g.add_edge((2, 3, 12))

        actual = g.egress(1)
        expected = [(1, 2, 10), (1, 3, 11)]
        self.assertEqual(actual, expected, 'should return ingress edges')

    def test_clone(self):
        g1 = Graph(False)
        g1.add_edge((1,2,10))
        g1.add_edge((2,3,20))
        g1.add_edge((3,1,30))

        g2 = g1.clone()
        g2.set_edge_value((1,2), 100)
        self.assertEqual(g1.get_edge_value((1,2)), 10,
                'should not have modified the value of the edge in g1')

        g2.add_vertex((3,4,40))
        self.assertFalse(g1.adjacent(3,4), 'g1 should not have vertex 4')
