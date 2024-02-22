INF = float('inf')

def floyd_warshall(graph):
    num_vertices = len(graph)
    
    # Initialize distance matrix
    dist = [[0 if i == j else graph[i][j] if graph[i][j] != 0 else INF for j in range(num_vertices)] for i in range(num_vertices)]

    # Print initial distance matrix
    print("Initial Distance Matrix:")
    print_matrix(dist)

    # Main loop of Floyd-Warshall algorithm
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
        print(f"\nAfter iteration {k + 1}:")
        print_matrix(dist)
    
    return dist

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Example graph adjacency matrix
graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

# Run Floyd-Warshall algorithm
shortest_paths = floyd_warshall(graph)

# Print final shortest paths matrix
print("\nFinal Shortest Paths Matrix:")
print_matrix(shortest_paths)
