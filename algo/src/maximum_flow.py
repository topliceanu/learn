# -*- coding: utf-8 -*-

from src.depth_first_search import dfs_paths


def ford_fulkerson_maximum_flow(g, s, t):
    """ Solves the maximum flow problem using the ford-fulkerson algorithm.

    Given a directed weighted graph g, a source vertex s and a sink vertex t,
    send as much flow as possible from s to t, knowing that each edge has a
    capacity value which is the maximum ammount of flow that the edge can
    accomodate.

    Discovered by Lester Ford and Delbert Fulkerson in 1956.

    Running time: O(m*f) where m - number of edges, f - value of max flow
                (Note! we assume edge capacities are integers)

    See: minimum cut problem (maximum flow reduces to minimum cut)
    See: http://web.stanford.edu/class/cs97si/08-network-flow-problems.pdf for reference implementation.
    See: http://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm

    TODO fix the case when there are pairs of nodes which have edges in both directions.

    Params:
        g: object, instance of src.graph.Graph
        s: str, name of the source vertex
        t: str, name of the sink vertex

    Returns:
        max_flow: int, the maximum ammount of flow you can send from s to t
        flow: object, instance of src.graph.Graph, each edge corresponds to the
            maximum flow passing through that edge.
    """
    # Add reversed edges to the original graph.
    h = g.clone()
    for e in h.get_edges():
        if not h.adjacent(e[1], e[2]):
            h.add_edge((e[1], e[0], e[2]))

    # Build a flow graph, initially set to 0.
    f = h.clone()
    [f.set_edge_value(e, 0) for e in f.get_edges()]

    # Finds a path from source to sink, making sure no vertex is visited twice
    # and no edge has negative weight.
    def find_path(source, end, path):
        if source == end:
            return path + [end]
        neighbours = h.neighbours(source)
        for neighbour in neighbours:
            e = (source, neighbour)
            if neighbour not in path and h.get_edge_value(e) > f.get_edge_value(e):
                result = find_path(neighbour, end, path[:] + [source])
                if result != None:
                    return result

    # Extract paths untill no path with non-negative edges can be found.
    while True:
        path = find_path(s, t, [])
        if path == None:
            break

        path_edges = [(path[i-1], path[i]) for i in range(1, len(path))]
        residuals = [h.get_edge_value(edge) - f.get_edge_value(edge) for edge in path_edges]
        path_flow = min(residuals)

        for edge in path_edges:
            reversed_edge = (edge[1], edge[0])
            f.set_edge_value(edge, f.get_edge_value(edge) + path_flow)

    # Build the final flow graph by subtracting flow for fake reverse edges
    # from the flow of original edges
    flow = g.clone()
    for edge in flow.get_edges():
        reversed_edge = (edge[1], edge[0])
        flow.set_edge_value(edge, f.get_edge_value(edge) - f.get_edge_value(reversed_edge))

    max_flow = sum([edge[2] for edge in flow.ingress(t)])

    return (max_flow, flow)


def min_cost_max_flow(g, s, t):
    """ A variant of the maximum flow problem where each edge, besides having
    a capacity, also has a cost.
    """
    # TODO
