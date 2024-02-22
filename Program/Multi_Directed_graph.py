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
