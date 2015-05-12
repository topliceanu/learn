# -*- coding: utf-8 -*-


class Backtracking(object):
    """ Strategy class encapsulating the backtracking metaheuristic. """

    def run(self):
        """ Executes the backtracking algorithm and returns the results. """
        seed = self.root()
        self.recurrence(seed)

    def recurrence(self, candidate):
        if not self.should_continue():
            return
        if self.reject(candidate):
            return
        if self.accept(candidate):
            return self.output(candidate)
        solution = self.first(candidate)
        while solution != None:
            self.recurrence(solution)
            solution = self.next(solution)

    def root(self):
        """ Return the partial candidate at the root of the search tree. """

    def reject(self, candidate):
        """ Returns true only if the candidate cannot form a correct solution. """

    def accept(self, candidate):
        """ Returns true if the candidate is a valid final solution. """

    def first(self, candidate):
        """ Generate the first extension of the given candidate partial
        solution.
        """

    def next(self, candidate):
        """ Generate the next alternative extension of a candidate, starting
        from the given extension.
        """

    def should_continue(self):
        """ Extend this method to stop the algorithm early. """

    def output(self, solution):
        """ Given the implementation a chance to work on a solution. """


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
        self.solutions = list()
        self.degree = degree
        self.stack = list()

    def output(self, solution):
        """ When a solutions is found, it is recorded. """
        self.solutions.append(solution)

    def get_solutions(self):
        """ Returns the list of found solutions. """
        return self.solutions

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
        """ Checks if the candidate is a finished solution. """
        return len(candidate) == self.degree and not self.reject(candidate)

    def should_continue(self):
        """ In this particular problem we are interested in all the solutions."""
        return True

    def root(self):
        """ Returns the start location for the first queen but computes all
        possible locations for this queen

        Returns:
            list, format [(x, y)]
        """
        positions = [(0, i) for i in range(self.degree)]
        for i in range(self.degree):
            self.stack.append([(0, i)])
        return self.next(None)

    def first(self, candidate):
        """ Generates all possible solution for this particular candidate and
        return only the first one.

        Params:
            candidate: list, format [(x, y)], only interested in variations in
                the position of the last queen.

        Returns:
            list, format [(x, y)]
        """
        if len(candidate) == self.degree:
            return None
        for i in range(self.degree):
            other = candidate[:]
            other.append((len(candidate), i))
            self.stack.append(other)
        return self.next(None)

    def next(self, candidate):
        """ """
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

class TwoSatSatisfaction(Backtracking):
    """ Solves the "two entites per clause" constraint satisfaction problem. """

class TravelingSalesman(Backtracking):
    """ Solves the traveling salesman using backtracking ie. in exponential time. """

class ConvexHull(Backtracking):
    """ Solves the convex hull problem (ie. Graham's Scan) """

class GeneratePermutations(Backtracking):
    """ Generates permutations using the backtracking problems. """
