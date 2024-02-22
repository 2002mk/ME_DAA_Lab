from collections import defaultdict, deque

class FordFulkerson:
    def __init__(self, graph):
        self.graph = graph
        self.num_vertices = len(graph)

    def bfs(self, source, sink, parent):
        visited = [False] * self.num_vertices
        queue = deque()
        queue.append(source)
        visited[source] = True

        while queue:
            u = queue.popleft()
            for v, capacity in enumerate(self.graph[u]):
                if not visited[v] and capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True
        return False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.num_vertices
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float('inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

def create_multistaged_graph(num_stages):
    graph = [[0] * num_stages for _ in range(num_stages)]

    print("Enter the connections between stages (Enter 0 if no connection exists):")
    for i in range(num_stages):
        for j in range(i + 1, num_stages):
            weight = int(input(f"Enter weight between stage {i + 1} and stage {j + 1}: "))
            graph[i][j] = weight
            graph[j][i] = weight  # Since the graph is undirected

    return graph

def display_multistaged_graph(graph):
    num_stages = len(graph)

    print("\nMulti-Staged Graph (Adjacency Matrix):")
    for i in range(num_stages):
        print(" ".join(map(str, graph[i])))

if __name__ == "__main__":
    num_stages = int(input("Enter the number of stages in the multi-staged graph: "))
    multistaged_graph = create_multistaged_graph(num_stages)
    display_multistaged_graph(multistaged_graph)



if __name__ == "__main__":
    # Example usage:
    num_stages = int(input("Enter the number of stages in the multi-staged graph: "))
    multistaged_graph = create_multistaged_graph(num_stages)
    display_multistaged_graph(multistaged_graph)


    ford_fulkerson = FordFulkerson(multistaged_graph)
    source= int(input("enter the source:"))
    sink=int(input("Enter the sink"))
    max_flow = ford_fulkerson.ford_fulkerson(source, sink)
    print("Maximum flow:", max_flow)
