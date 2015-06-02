# -*- coding: utf-8 -*-


class Backtracking(object):
    """ Strategy class encapsulating the backtracking metaheuristic.

    See generic descriptions of the method:
    http://en.wikipedia.org/wiki/Backtracking
    http://web.cse.ohio-state.edu/~gurari/course/cis680/cis680Ch19.html#QQ1-51-128
    """

    def run(self):
        """ Executes the backtracking algorithm and returns the results. """
        seed = self.root()
        self.recurrence(seed)

    def recurrence(self, candidate):
        """ Main recurrence of the algorithm. Do NOT extend this! """
        if self.should_continue() is False:
            return
        if self.reject(candidate):
            return
        if self.accept(candidate):
            self.output(candidate)
        solutions = self.extend(candidate)
        for solution in solutions:
            self.recurrence(solution)

    def root(self):
        """ Return the partial candidate at the root of the search tree,
        ie. the seed!
        """

    def should_continue(self):
        """ Hook to allow implementation to stop the algorithm early. Defaults
        to True, meaning explore the entire solutions space.
        """
        return True

    def accept(self, candidate):
        """ Returns true if the candidate is a valid final solution.

        Returns:
            bool, True if candidate is valid
        """

    def output(self, solution):
        """ Gives the implementation a chance to process a solution. """

    def reject(self, candidate):
        """ Returns true only if the candidate cannot possibly form a correct
        solution.

        Returns:
            bool
        """

    def extend(self, candidate):
        """ Extends the of the given candidate partial solution. """


class QueenPuzzle(Backtracking):
    """ Solves the eight queen puzle.

    The format of the candidates for a problem is [(x,y)], each queen
    represents a pair of coordinates (x, y), where x,y in [0,7].

    See: http://en.wikipedia.org/wiki/Eight_queens_puzzle

    Attrs:
        solutions: list, collects all the solutions.
        degree: int, the size of square board (for instance 8 for a chess board)
    """
    def __init__(self, degree):
        self.solutions = []
        self.degree = degree

    def output(self, solution):
        """ When a solutions is found, it is recorded. """
        self.solutions.append(solution)

    def reject(self, candidate):
        """ Rejects the candidate subproblem is at least two queens are on the
        same line, column or diagonal.

        Params:
            candidate: list, format [(i, j)]

        Returns:
            bool, True if solution is rejected
        """
        diag1 = set([]) # First diagonal is (n-m) + x = 0. We only store (n-m)
        diag2 = set([]) # Second diagonal is (n+m) -x = 0. We only store (n+m)
        rows = set([]) # rows where the queens are positioned.
        cols = set([]) # columns where the queens are positioned.

        # No two queens should be on the same line or diagonals.
        for pair in candidate:
            (i, j) = pair
            if j-i in diag1:
                return True
            else:
                diag1.add(j-i)
            if j+i in diag2:
                return True
            else:
                diag2.add(j+i)
            if i in rows:
                return True
            else:
                rows.add(i)
            if j in cols:
                return True
            else:
                cols.add(j)
        return False

    def accept(self, candidate):
        """ Checks if the candidate is a finished solution. Accept is always
        called after reject() so if it reached this far then this solution is
        valid.
        """
        return len(candidate) == self.degree

    def should_continue(self):
        """ In this particular problem we are interested in all the solutions."""
        return True

    def root(self):
        """ Returns the start location for the first queen but computes all
        possible locations for this queen

        Returns:
            list, format [(x, y)]
        """
        return []

    def extend(self, candidate):
        """ Generates all possible solution for this particular candidate and
        return only the first one.
        This method is interested in variations in the position of the last queen.

        Params:
            candidate: list, format [(x, y)]

        Returns:
            list, of lists of candidates extended from current one.
                Format [[(x, y),..],..]
        """
        if len(candidate) == 0:
            return [[(0, i)] for i in range(self.degree)]

        (last_queen_row, _) = candidate[-1]

        if last_queen_row == self.degree - 1:
            return []

        candidates = []
        for i in range(self.degree):
            tmp = candidate[:]
            tmp.append((last_queen_row + 1, i))
            if not self.reject(tmp):
                candidates.append(tmp)
        return candidates


class TravelingSalesman(Backtracking):
    """ Solves the traveling salesman using backtracking ie. in exponential time.

    Attrs:
        solution: list, each item represents a city id. This field keep the best solution
        min_cost: float, stores the cost of the solution
        graph: instance of src.graph.Graph
    """

    def __init__(self, graph):
        self.solution = []
        self.min_cost = float('inf')
        self.graph = graph

    def root(self):
        return []

    def reject(self, candidate):
        """ Reject a candidate which goes through the same city multiple times. """
        return len(set(candidate)) != len(candidate)

    def accept(self, candidate):
        """ Accepting only the candidate who traverse all vertices of the graph only once. """
        return len(candidate) == len(set(candidate)) == len(self.graph.get_vertices())

    def output(self, candidate):
        """ The received candidate traverses all vertices in the graph only
        once. To produce a cycle, this method tests if first city is reachable
        from the last city in the candidate. If it is, it adds it to the
        solution, otherwise it ignores the solution alltoghether.
        """
        if not self.graph.adjacent(candidate[-1], candidate[0]):
            return
        candidate.append(candidate[0])

        cost = 0
        for i in range(len(candidate)-1):
            cost += self.graph.get_edge_value((candidate[i], candidate[i+1]))
        if cost < self.min_cost:
            self.solution = candidate
            self.min_cost = cost

    def extend(self, candidate):
        """ Expand the given candidate by adding all cities which can be
        connected.

        Two case: initially, when the candidate is empty, populate with all
        vertices in the graph. Otherwise, produce a candidate solution for
        each city which connects to the last city in the current partial
        solution and which hasn't been visited so far.

        Returns:
            list, of lists, format [[cities...]]
        """
        if len(candidate) == 0:
            return [[i] for i in self.graph.get_vertices()]

        solutions = []
        last_city = candidate[-1]
        for city in self.graph.neighbours(last_city):
            if city not in candidate:
                tmp = candidate[:]
                tmp.append(city)
                solutions.append(tmp)
        return solutions

# TODO
#class TwoSatSatisfaction(Backtracking):
#    """ Solves the "two entites per clause" constraint satisfaction problem. """
#
#class ConvexHull(Backtracking):
#    """ Solves the convex hull problem (ie. Graham's Scan) """
#
#class GeneratePermutations(Backtracking):
#    """ Generates permutations using the backtracking problems. """
