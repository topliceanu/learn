# -*- coding: utf-8 -*-


class Graph:
    """ Data structure to hold graph data using adjacency lists. """

    def __init__(self, vertices=[], edges=[], edges_by_vertex={}, vertices_by_edge={}):
        self.vertices = vertices
        self.edges = edges
        self.edges_by_vertex = edges_by_vertex
        self.vertices_by_edge = vertices_by_edge

    def get_edges(self, vertex):
        self.edges_by_vertex[vertext]

    def get_vertices(self, edge):
        self.vertices_by_edge[edge]
