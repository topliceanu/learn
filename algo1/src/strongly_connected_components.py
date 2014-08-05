def scc(g):
    """ Computes strongly connected components of a acyclic directed graph.
    Uses the Kosaraju two-pass algorithm.
    1. reverse all the edges in a graph.
    2. run DFS on the reverse graph.
    3. run DFS on the normal graph.
    """
