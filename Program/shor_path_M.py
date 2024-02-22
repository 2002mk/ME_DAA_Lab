# Define a function to find the minimum cost and optimal path in a multistage graph
def min_cost_multistage_graph(graph, stages):
    num_stages = len(stages)
    num_nodes = len(graph)

    # Initialize cost and parent arrays
    cost = [float('inf')] * num_nodes
    parent = [None] * num_nodes

    # Set costs for nodes in the first stage to 0
    for node in stages[0]:
        cost[node] = 0

    # Dynamic Programming approach to calculate minimum cost
    for i in range(1, num_stages):
        for node in stages[i]:
            min_cost = float('inf')
            for parent_node in stages[i - 1]:
                edge_cost = graph[parent_node][node]
                total_cost = cost[parent_node] + edge_cost
                if total_cost < min_cost:
                    min_cost = total_cost
                    parent[node] = parent_node
            cost[node] = min_cost

    # Reconstruct the shortest path
    path = [None] * num_stages
    path[num_stages - 1] = stages[num_stages - 1][0]
    for i in range(num_stages - 2, -1, -1):
        path[i] = parent[path[i + 1]]

    return cost[stages[num_stages - 1][0]], path

# Get input from the user
num_nodes = int(input("Enter the number of nodes: "))
graph = [[0] * num_nodes for _ in range(num_nodes)]

# Input weights for edges
for i in range(num_nodes):
    edges = input(f"Enter weights for edges from node {i} (space-separated, use 0 for no connection): ").split()
    graph[i] = [int(weight) for weight in edges]

num_stages = int(input("Enter the number of stages: "))
stages = [list(map(int, input(f"Enter nodes for stage {i} (space-separated): ").split())) for i in range(num_stages)]

# Call the min_cost_multistage_graph function with user input
min_cost, optimal_path = min_cost_multistage_graph(graph, stages)

# Print the results
print(f"Minimum cost: {min_cost}")
print("Optimal Path:", optimal_path)