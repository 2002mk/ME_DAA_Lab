class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]
    def is_valid_edge(self, u, v, capacity):
        return 0 <= u < self.V and 0 <= v < self.V and capacity >= 0
    def add_edge(self, u, v, capacity):
        if self.is_valid_edge(u, v, capacity):
            self.graph[u][v] = capacity
    def print_solution(self, flow):
        print("Edge\tFlow")
        for i in range(self.V):
            for j in range(self.V):
                if flow[i][j] > 0:
                   print(f"{i} -> {j}\t{flow[i][j]}")
    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.V
        max_flow = 0
        flow = [[0] * self.V for _ in range(self.V)]
        while self.bfs(source, sink, parent):
            path_flow = float("inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = parent[v]
        # Update the residual capacities of edges along the path
        v = sink
        while v != source:
            u = parent[v]
            self.graph[u][v] -= path_flow
            self.graph[v][u] += path_flow
            v = parent[v]
        # Reset parent array for next BFS
        parent = [-1] * self.V
        self.print_solution(flow)
        return max_flow
    def bfs(self, source, sink, parent):
        visited = [False] * self.V
        queue = [source]
        visited[source] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if not visited[ind] and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                parent[ind] = u
        return visited[sink]
if __name__ == "__main__":
    vertices = int(input("Enter the number of vertices: "))
    g = Graph(vertices)
    edges = int(input("Enter the number of edges: "))
    print("Enter the edges (source, destination, capacity): ")
    for _ in range(edges):
        u, v, capacity = map(int, input().split())
        g.add_edge(u, v, capacity)
    source = int(input("Enter the source node: "))
    sink = int(input("Enter the sink node: "))
    max_flow = g.ford_fulkerson(source, sink)
    print(f"The maximum flow is {max_flow}")
