class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_list = [[] for _ in range(num_nodes)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def print_graph(self):
        for node in range(self.num_nodes):
            print(f"Adjacent nodes of node {node}: {self.adj_list[node]}")

    def print_vertex_cover(self):
        visited = [False] * self.num_nodes
        for u in range(self.num_nodes):
            if not visited[u]:
                for v in self.adj_list[u]:
                    if not visited[v]:
                        visited[u] = True
                        visited[v] = True
                        break
        print("Vertex Cover:")
        for i in range(self.num_nodes):
            if visited[i]:
                print(i, end=" ")
        print()

if __name__ == "__main__":
    num_nodes = int(input("Enter the number of nodes: "))
    num_edges = int(input("Enter the number of edges: "))
    
    graph = Graph(num_nodes)

    print("Enter edges (node1 node2):")
    for _ in range(num_edges):
        u, v = map(int, input().split())
        graph.add_edge(u, v)

    print("\nGraph:")
    graph.print_graph()
    graph.print_vertex_cover()
