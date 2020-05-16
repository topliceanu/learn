# -*- coding: utf-8 -*-

# Recap graph algorithms:

# DFS vs BFS
#  - DFS does the adjacent nodes before it does the node itself.
#  - BFS does the node itself before the adjacent ones.
# BFS is used for computing shortest path to a vertex. Not DFS.

def dfs(src):
    """ Depth-first search traversal, returns all the nodes in the graph that
    are reachable from src
    Complexity: O(m)
    Args:
        src, Vertex
    Returns:
        list of Vertex
    """
    visited = set([])
    stack = [src]
    while len(stack) != 0:
        node = stack.pop()
        visited.add(node)
        for adjacent in node.adjacent:
            if adjacent in visited:
                continue
            stack.append(adjacent)

def dfs_rec(src, visited):
    """ Same as DFS but with a recursive implementation.
    Params:
        src, Vertex
        visited, set of Vertex
    """
    for node in src.adjacent:
        dfs_rec(node, visited)
    if src in visited:
        return
    visited.add(src)

def bfs(src):
    """ Breadth-first search: same as above but using stack instead of a queue."""
    visited = set([])
    queue = [src]
    while len(queue) != 0:
        node = queue.remove(0) # queue.dequeue
        visited.add(node)
        for adjacent in node.adjacent:
            if adjacent in visited:
                continue
            queue.append(adjacent)

def dfs_rec(src, visited):
    """ Same as DFS but with a recursive implementation.
    Params:
        src, Vertex
        visited, set of Vertex
    """
    if src in visited:
        return
    visited.add(src)
    for node in src.adjacent:
        dfs_rec(node, visited)

def bfs_shortest_path(src, dest):
    # First, BFS the graph to assign distance values to each node.
    src.value = 0
    visited = []
    queue = [src]
    while len(queue) != 0:
        node = queue.pop(0)
        for adjacent in node.adjacent:
            if adjacent in visited:
                continue
            adjacent.value = node.value + 1
            queue.append(adjacent)
            visited.add(adjacent)

    # Second, backtrack from dest to source to build one path.
    # You can do all the paths by collecting all adjacent nodes.
    if dest.value == None:
        return [] # No path from source
    path = []
    node = dest
    current_length = dest.value
    while current_length >= 0:
        path.push(node)
        for adjacent in node.adjacent:
            if adjacent.value == current_length - 1:
                node = adjacent
                current_lenght -= 1
                break
    return path.reverse()

def connected_components_in_undirected_graph(vertices):
    def dfs(vertex, index):
        """ Recursive DFS traverses all reachable vertices from vertex
        and assigns index to them.
        """
        queue = [vertex]
        while len(queue) != 0:
            other = queue.pop(0) # dequeue
            if other.value != None:
                continue
            other.value = index
            for adjacent in other.adjacent:
                queue.append(adjacent)

    # label each node with the index of the connected component they belong to.
    current_index = 0
    for vertex in vertices:
        bfs(vertex,  current_index)
        current_index += 1

    # return the number of components
    return current_index

class TopSortNode(object):
    def __init__(self, key):
        self.key = key
        self.visited = False
        self.label = None

def topological_ordering_in_directing_graph(vertices):
    """ Conceptual algorithm for topological ordering:
    1. pick a sync vertex - there may be many such syncs.
        A sync vertex is a vertex with only inword edges in a directed graph.
    2. label that vertex with the current index (initialised with the number of vertices)
    3. remove that vertex from the graph, along with any edges, inword or outward.
    4. start over from 1.

    Actual algorithm using DFS:
    1. Pick a random unexplored vertex to start.
    2. DFS from that vertex until you reach an unexplored sync, ie. you can't proceed anymore.
    3. Assign that the current label (initialized with the number of nodes) then decrement the current label.
    4. Start again from 1 as long as there are unexplored vertices in the graph

    Args:
        vertices, list of TopSortNode
    """
    label = len(vertices) - 1
    global label

    def dfs_and_label_sync(vertex):
        vertex.visited = true
        for adjacent in vertex.adjacent:
            dfs_and_label_sync(adjacent)
        vertex.label = label
        label -= 1
        return label

    for vertex in verticies:
        if vertex.visited:
            continue
        dfs_and_label_sync(vertex)

    # collect all the vertices in topological order.
    for v in vertices:
        v.visited = False
    order = [None] * len(vertices)
    queue = [vertices[0]]
    while len(queue) != 0:
        vertex = queue.pop(0) # dequeue
        if vertex.visited:
            continue
        order[vertex.label] = vertex
        for adjacent in vertex.adjacent:
            queue.append(ajacent)
    return order

