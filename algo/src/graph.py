# -*- coding: utf-8 -*-

import math


class Graph:
    """ Base data structure to hold graph data using adjacency lists.

    Uses the adjacency list paradigm to save on space.

    Attributes:
        directed: bool, marking whether or not the graph is directed.
        table: dict, with all vertices in the graph as keys. The format is
            {tail: {head: edge_value}
        values: dict, holding the values of vertices. Format: {vertex: value}
        incident_vertices: dict, holds a set of ingress vertices for each vertex
            in the graph. Format {head: {tails}}
    """

    def __init__(self, directed=False):
        # Marks whether or not the graph is directed. Defaults to False.
        self.directed = directed

        # Dict structure to hold the graph. Format {tail: {head: value}}
        self.table = {}

        # Dict structure to hold the vertices values.
        self.values = {}

        # Dict to hold ingress vertices. Format {head: {tails}}
        self.incident_vertices = {}

    def split_edge(self, edge):
        """ Disambiguate edges.

        Args:
            edge: tuple, format (tail, head, value). Some edges may not
                have values, in this case True is used.

        Returns:
            A tuple with format (tail, head, value).
        """

        tail = edge[0]
        head = edge[1]
        if len(edge) == 2:
            value = True
        else:
            value = edge[2]
        return (tail, head, value)

    def add_vertex(self, vertex):
        """ Adds vertex to the graph data structure. """
        if vertex not in self.table:
            self.table[vertex] = {}
        if vertex not in self.incident_vertices:
            self.incident_vertices[vertex] = set()

    def add_edge(self, edge):
        """ Adds edge to the graph data structure.

        If the graph is undirected, both edge and reverse edge will be stored.

        Args:
            edge: tuple of format (tail, head, value)
        """
        (tail, head, value) = self.split_edge(edge)

        self.add_vertex(head)
        self.add_vertex(tail)

        # Give up in case this is a self edge.
        if head == tail:
            return

        self.table[tail][head] = value
        self.incident_vertices[head].add(tail)
        if self.directed == False:
            self.table[head][tail] = value
            self.incident_vertices[tail].add(head)

    def get_vertices(self):
        """ Returns all vertices in the stored graph. """
        return self.table.keys()

    def get_edges(self):
        """ Return all edges in the stored graph.

        If the graph is undirected, reverse edges will not be returned.
        To speed things up, we use a set in case the graph is not directed.

        Returns:
            A list of tuples of format [(tail, head, value)]
        """
        if self.directed == False:
            output = set()
            for tail, edges in self.table.iteritems():
                for head, value in edges.iteritems():
                    t = sorted([tail, head])
                    t.append(value)
                    output.add(tuple(t))
            output = list(output)
        else:
            output = []
            for tail, edges in self.table.iteritems():
                for head, value in edges.iteritems():
                    output.append((tail, head, value))
        return output

    def adjacent(self, tail, head):
        """ Returns whether or not there is an edge between tail and head. """
        if tail in self.table:
            if head in self.table[tail]:
                return True
        return False

    def neighbours(self, vertex):
        """ Returns a list of all vertices reachable from vertex.

        Args:
            vertex: str, name of vertex whos neighbours we want.

        Returns:
            A list of neighbouring vertices.
        """
        if vertex not in self.table:
            return []
        else:
            return self.table[vertex].keys()

    def incident(self, vertex):
        """ Returns a list of all vertices from which you can reach vertex.

        This is most relevant for directed graphs but can work on undirected
        as well.
        """
        if vertex not in self.incident_vertices:
            return []
        return list(self.incident_vertices[vertex])

    def ingress(self, vertex):
        """ Return all the edges whose head is vertex. """
        if vertex not in self.incident_vertices:
            return []

        output = []
        for tail in self.incident_vertices[vertex]:
            output.append((tail, vertex, self.table[tail][vertex]))
        return output

    def egress(self, vertex):
        """ Return all the edges whose tail is vertex. """
        if vertex not in self.table:
            return []

        edges = []
        for head, value in self.table[vertex].iteritems():
            edges.append((vertex, head, value))
        return edges

    def get_edge_value(self, edge):
        """ Return value of the edge given in format (tail, head). """
        (tail, head, __) = self.split_edge(edge)
        if self.adjacent(tail, head):
            return self.table[tail][head]
        else:
            return None

    def set_edge_value(self, edge, newValue):
        """ Set value of edge to be newValue. """
        (tail, head, _) = self.split_edge(edge)

        if self.adjacent(tail, head):
            self.table[tail][head] = newValue
        if self.directed == False:
            if self.adjacent(head, tail):
                self.table[head][tail] = newValue

    def get_vertex_value(self, vertex):
        """ Return the value corresponding to the vertex name. """
        if vertex in self.values:
            return self.values[vertex]
        return None

    def set_vertex_value(self, vertex, newValue):
        """ Update value of vertex with the newValue. """
        self.values[vertex] = newValue

    def remove_edge(self, edge):
        """ Removes an edge from the graph.

        If the graph is not directed the reverse edge will be removed as well.

        Args:
            edge: tuple for format (tail, head, value) representing a graph edge
        """
        (tail, head, value) = self.split_edge(edge)
        if tail in self.table:
            if head in self.table[tail]:
                del self.table[tail][head]
                self.incident_vertices[head].remove(tail)
        if self.directed == False:
            if head in self.table:
                if tail in self.table[head]:
                    del self.table[head][tail]
                    self.incident_vertices[tail].remove(head)

    def remove_vertex(self, vertex):
        """ Removes vertex and it's adjacent and incident edges.

        Graph data is stored in three structures: table, values and
        incident_vertices. All these structures have to be cleaned up.
        """
        if vertex not in self.table:
            return

        if vertex in self.values:
            del self.values[vertex]

        for head in self.table[vertex]:
            self.incident_vertices[head].remove(vertex)

        for tail in self.incident_vertices[vertex]:
            del self.table[tail][vertex]

        del self.table[vertex]
        del self.incident_vertices[vertex]

    def rename_vertex(self, old, new):
        """ Renames old vertex into new vertex.

        Args:
            old: str, old name of the vertex.
            new: str, the new name of the vertex.
        """
        if old not in self.table:
            return

        if new in self.table:
            self.table[new] = dict(self.table[old].items() +self.table[new].items())
        else:
            self.table[new] = self.table[old]
        del self.table[old]

        for tail, edges in self.table.iteritems():
            if tail == new and new in edges:
                del self.table[tail][new]
            if old in edges:
                if tail != new:
                    self.table[tail][new] = self.table[tail][old]
                del self.table[tail][old]

    def clone(self):
        """ Clones the current graph, makes sure the mutable properties of the
        input graph are not modified by operations in the second graph.
        """
        return Graph.build(self.get_vertices(), self.get_edges(), self.directed)

    @staticmethod
    def build(vertices=[], edges=[], directed = False):
        """ Builds a graph from the given vertices and edges.

        Args:
            vertices: list of immutable vertex names.
            edges: list of edges of format (tail, head, value)
            directed: bool indicating whether the graph is directed or not.

        Returns:
            An instance of this current Graph class.
        """
        g = Graph(directed)
        for vertex in vertices:
            g.add_vertex(vertex)
        for edge in edges:
            g.add_edge(edge)
        return g

    @staticmethod
    def build_from_coords(coords=[], directed=False, distance=None):
        """ Method builds a Graph instance from a list of point coordinates.

        Args:
            coords: list of tuples, format [(name, x, y)]

        Returns:
            object, instance of src.graph.Graph
        """
        if distance == None:
            def distance(p1, p2):
                """ Default is euclidian distance. """
                return float(math.sqrt((p1[1] - p2[1])**2 + (p1[2] - p2[2])**2))

        g = Graph.build(directed=directed)
        for p1 in coords:
            for p2 in coords:
                if p1 == p2:
                    continue
                g.add_edge((p1[0], p2[0], distance(p1, p2)))

        return g
