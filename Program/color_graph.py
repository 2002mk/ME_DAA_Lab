import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def is_safe(self, v, color, c):
        for i in range(self.vertices):
            if self.graph[v][i] == 1 and color[i] == c:
                return False
        return True

    def graph_coloring_util(self, m, color, v):
        if v == self.vertices:
            return True

        for c in range(1, m + 1):
            if self.is_safe(v, color, c):
                color[v] = c
                if self.graph_coloring_util(m, color, v + 1):
                    return True
                color[v] = 0

    def graph_coloring(self, m):
        color = [0] * self.vertices
        if not self.graph_coloring_util(m, color, 0):
            print("No solution exists")
            return False

        print("Solution exists with the following coloring:")
        for c in color:
            print(c, end=" ")

        # Plotting the colored graph
        G = nx.Graph()
        for i in range(self.vertices):
            G.add_node(i)
        for i in range(self.vertices):
            for j in range(i + 1, self.vertices):
                if self.graph[i][j] == 1:
                    G.add_edge(i, j)

        node_colors = [color[i] for i in range(self.vertices)]
        nx.draw(G, with_labels=True, node_color=node_colors, cmap=plt.cm.rainbow, node_size=1000)
        plt.show()
        return True

if __name__ == "__main__":
    # Get input from the user
    vertices = int(input("Enter the number of vertices: "))
    edges = int(input("Enter the number of edges: "))

    g = Graph(vertices)

    # Get edges from the user
    print("Enter the edges (vertex1 vertex2):")
    for _ in range(edges):
        u, v = map(int, input().split())
        g.add_edge(u, v)

    m = 3  # Number of colors
    g.graph_coloring(m)
