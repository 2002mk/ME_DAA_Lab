INF = float('inf')

def floyd_warshall(graph):
    num_stages = len(graph)
    
    # Initialize distance matrix
    dist = [[0 if i == j else graph[i][j] if graph[i][j] != 0 else INF for j in range(num_stages)] for i in range(num_stages)]

    # Print initial distance matrix
    print("Initial Distance Matrix:")
    print_matrix(dist)

    # Main loop of Floyd-Warshall algorithm
    for k in range(num_stages):
        for i in range(num_stages):
            for j in range(num_stages):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
        print(f"\nAfter stage {k + 1}:")
        print_matrix(dist)
    
    return dist

def print_matrix(matrix):
    for row in matrix:
        print(row)
"""
# Example usage with multi-staged graph
if __name__ == "__main__":
    graph = [
        [0, 5, INF, INF],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [10, INF, INF, 0]
    ]

    # Run Floyd-Warshall algorithm
    shortest_paths = floyd_warshall(graph)

    # Print final shortest paths matrix
    print("\nFinal Shortest Paths Matrix:")
    print_matrix(shortest_paths)
"""

def create_multistaged_graph(num_stages):
    graph = [[0 if i == j else float('inf') for j in range(num_stages)] for i in range(num_stages)]

    print("Enter the weights between stages (Enter 'inf' for non-weighted edges):")
    for i in range(num_stages):
        for j in range(i + 1, num_stages):
            weight = input(f"Enter weight between stage {i + 1} and stage {j + 1}: ")
            if weight == 'inf':
                graph[i][j] = float('inf')
                graph[j][i] = float('inf')
            else:
                graph[i][j] = int(weight)
                graph[j][i] = int(weight)  # Since the graph is undirected

    return graph

def display_multistaged_graph(graph):
    num_stages = len(graph)

    print("\nMulti-Staged Graph (Adjacency Matrix):")
    for i in range(num_stages):
        print(" ".join(['inf' if val == float('inf') else str(val) for val in graph[i]]))

if __name__ == "__main__":
    num_stages = int(input("Enter the number of stages in the multi-staged graph: "))
    multistaged_graph = create_multistaged_graph(num_stages)
    display_multistaged_graph(multistaged_graph)


    shortest_paths = floyd_warshall(multistaged_graph)

    print("\nFinal Shortest Paths Matrix:")
    print_matrix(shortest_paths)