# -*- coding: utf-8 -*-


class Graph:
    """ Data structure to hold graph data using adjacency lists.
    Uses the adjacency list paradigm.

    TODO add implementation and tests for all these methods.
    """

    # list() - list of vertex names.
    vertices = []

    # list(tuples()) - list of tuples, each tuple represents
    # the vertex ends of an edge.
    edges = []

    def __init__(self, vertices=[], edges=[]):
        """
        """
        self.vertices = vertices
        self.edges = edges

    # The basic operations provided by a graph data structure:

    def adjacent(x, y):
        """ Tests whether there is an edge from node x to node y."""
        pass

    def neighbors(x):
        """ Lists all nodes y such that there is an edge from x to y. """
        pass

    def add_edge(x, y):
        """ Adds to G the edge from x to y, if it is not there. """
        pass

    def delete_edge(x, y):
        """ Removes the edge from x to y, if it is there. """
        pass

    def add_vertex(x):
        """ Add a vertex to the graph. """
        pass

    def delete_vertex(x):
        """ Removes a vertex and all adjacent edges from the graph. """
        pass

    def get_vertex_value(x):
        pass

    def set_vertex_value():
        pass

    def get_edge_value(x, y):
        pass

    def set_edge_value(x, y, v):
        pass


class DirectedGraph(Graph):
    pass
