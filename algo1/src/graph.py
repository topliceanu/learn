# -*- coding: utf-8 -*-

class Graph:
    """ Base data structure to hold graph data using adjacency lists.
    Uses the adjacency list paradigm to save on space.
    """

    # Representation of the graph as a dict of dicts.
    table = {}

    # Whether or not the current graph is directed or not.
    directed = False

    def __init__(directed):
        self.directed = directed

    def split_edge(self, edge):
        tail = edge[0]
        head = edge[1]
        if len(edge) == 2:
            value = True
        else:
            value = edge[2]
        return (tail, head, value)

    def add_edge(self, edge):
        (tail, head, value) = self.split_edge(edge)

        self.add_vertex(head)
        self.add_vertex(tail)
        self.table[tail] = {head: value}

        if self.directed == False:
            self.table[head] = {tail: value}

    def remove_edge(self, edge):
        (tail, head, value) = self.split_edge(edge)
        if tail in self.table:
            if head in self.table[tail]:
                del self.table[tail][head]
        if self.directed == False:
            if head in self.table:
                if tail in self.table[head]:
                    del self.table[head][tail]

    def inverse_edge(self, edge):
        (tail, head, value) = self.split_edge(edge)
        return (head, tail, value)

    def add_vertex(self, vertex):
        if self.table[vertex] is None:
            self.table[vertex] = {}

    def remove_vertex(self, vertex):
        if vertex not in self.table:
            return

        for head, value in self.table[vertex].iteritems():
            del self.table[head][vertex]
        del self.table[vertex]

    def adjacent(self, head, tail):
        return self.table[head][tail] != None

    def neighbours(self, vertex):
        if self.table[vertex] is None:
            return []
        else:
            return sel.table[vertex].keys()

    def get_edge_value(self, edge):
        (tail, head) = self.split_edge(edge)
        if self.adjacent(tail, head):
            return self.table[tail][head]

    def rename_vertex(self, old, new):
        if old not in self.table:
            return

        if old == new:
            return

        self.table[new] = self.table[old]
        del self.table[old]

        for tail, edges in self.table.iteritems():
            for head, value in edges.iteritems():
                if head == old:
                    self.table[tail][new] = value
                    del self.table[tail][old]

    def clean_self_edges(self):
        for tail, edges in self.table.iteritems():
            for head, value in edges.iteritems():
                if head == tail:
                    del self.table[tail][head]

    @staticmethod
    def build(vertices, edges, directed = False):
        g = Graph(directed)
        for vertex in vertices:
            g.add_vertex(vertex)
        return g
