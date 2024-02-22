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
