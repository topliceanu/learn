# -*- coding: utf-8 -*-

class Graph:
    """ Base data structure to hold graph data using adjacency lists.
    Uses the adjacency list paradigm to save on space.
    """

    def __init__(self, directed=False):
        self.directed = directed
        self.table = {}

    def split_edge(self, edge):
        tail = edge[0]
        head = edge[1]
        if len(edge) == 2:
            value = True
        else:
            value = edge[2]
        return (tail, head, value)

    def add_vertex(self, vertex):
        if vertex not in self.table:
            self.table[vertex] = {}

    def add_edge(self, edge):
        (tail, head, value) = self.split_edge(edge)

        self.add_vertex(head)
        self.add_vertex(tail)
        self.table[tail][head] = value

        if self.directed == False:
            self.table[head][tail] = value

    def get_vertices(self):
        return self.table.keys()

    def adjacent(self, tail, head):
        if tail in self.table:
            if head in self.table[tail]:
                return True
        return False

    def neighbours(self, vertex):
        if vertex not in self.table:
            return []
        else:
            return self.table[vertex].keys()

    def get_edge_value(self, edge):
        (tail, head, __) = self.split_edge(edge)
        if self.adjacent(tail, head):
            return self.table[tail][head]
        else:
            return None

    def set_edge_value(self, edge, value):
        pass

    def remove_edge(self, edge):
        (tail, head, value) = self.split_edge(edge)
        if tail in self.table:
            if head in self.table[tail]:
                del self.table[tail][head]
        if self.directed == False:
            if head in self.table:
                if tail in self.table[head]:
                    del self.table[head][tail]

    def remove_vertex(self, vertex):
        if vertex not in self.table:
            return
        del self.table[vertex]

        for tail, edges in self.table.iteritems():
            if vertex in edges:
                del self.table[tail][vertex]

    def rename_node(self, old, new):
        if old not in self.table:
            return

        self.table[new] = self.table[old]
        del self.table[old]

        for tail, edges in self.table.iteritems():
            if old in edges:
                self.table[tail][new] = self.table[tail][old]
                del self.table[tail][old]

    @staticmethod
    def build(vertices, edges, directed = False):
        g = Graph(directed)
        for vertex in vertices:
            g.add_vertex(vertex)
        return g
