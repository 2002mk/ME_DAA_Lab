from itertools import combinations
from pulp import LpMaximize, LpProblem, LpVariable, lpSum

class MaximumClique:
    def __init__(self, graph):
        self.graph = graph
        self.nodes = range(len(graph))
        self.model = LpProblem(name="maximum_clique", sense=LpMaximize)
        self.x = LpVariable.dicts("x", self.nodes, cat="Binary")

    def add_constraints(self):
        for i, j in combinations(self.nodes, 2):
            if not self.graph[i][j]:
                self.model += self.x[i] + self.x[j] <= 1

    def solve(self):
        self.model += lpSum(self.x)
        self.add_constraints()
        self.model.solve()

    def get_solution(self):
        return [i for i in self.nodes if self.x[i].value() == 1]

# Example usage:
if __name__ == "__main__":
    # Example graph represented as an adjacency matrix
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 0]
    ]

    maximum_clique_solver = MaximumClique(graph)
    maximum_clique_solver.solve()
    max_clique = maximum_clique_solver.get_solution()
    print("Maximum clique:", max_clique)
