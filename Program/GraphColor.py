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
        return True

if __name__ == "__main__":
    # Example usage:
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    m = 3  # Number of colors
    g.graph_coloring(m)
