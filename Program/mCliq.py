from itertools import combinations
from pulp import LpMaximize, LpProblem, LpVariable, lpSum
import networkx as nx
import matplotlib.pyplot as plt

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

if __name__ == "__main__":
    # Get input from the user
    num_nodes = int(input("Enter the number of nodes: "))
    print("Enter the adjacency matrix (0 or 1) for the graph:")
    graph = []
    for _ in range(num_nodes):
        row = input().split()
        row = [int(val) for val in row]
        graph.append(row)

    # Solve the maximum clique problem
    maximum_clique_solver = MaximumClique(graph)
    maximum_clique_solver.solve()
    max_clique = maximum_clique_solver.get_solution()
    print("Maximum clique:", max_clique)

    # Create a NetworkX graph for visualization
    G = nx.Graph()
    G.add_nodes_from(range(num_nodes))
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if graph[i][j] == 1:
                G.add_edge(i, j)

    # Plot the graph
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=800, font_size=12, font_weight='bold')
    plt.title("Input Graph")
    plt.show()
