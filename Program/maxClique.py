MAX = 100

# Stores the vertices
store = [0] * MAX

# Graph
graph = [[0] * MAX for _ in range(MAX)]

# Degree of the vertices
d = [0] * MAX

# Function to check if the given set of vertices
# in the store array is a clique or not
def is_clique(b):
    # Run a loop for all the set of edges
    # for the select vertex
    for i in range(1, b):
        for j in range(i + 1, b):
            # If any edge is missing
            if graph[store[i]][store[j]] == 0:
                return False
    return True

# Function to print the clique
def print_cli(n):
    for i in range(1, n):
        print(store[i], end=" ")
    print(",", end=" ")

# Function to find all the cliques of size s
def findCliques(i, l, s):
    # Check if any vertices from i+1 can be inserted
    for j in range(i + 1, n - (s - l) + 1):
        # If the degree of the graph is sufficient
        if d[j] >= s - 1:
            # Add the vertex to store
            store[l] = j
            # If the graph is not a clique of size k
            # then it cannot be a clique by adding another edge
            if is_clique(l + 1):
                # If the length of the clique is still less than the desired size
                if l < s:
                    # Recursion to add vertices
                    findCliques(j, l + 1, s)
                # Size is met
                else:
                    print_cli(l + 1)

# Driver code
if __name__ == "__main__":
    edges = int(input("Enter the number of edges: "))
    print("Enter the edges (format: vertex1 vertex2):")
    for _ in range(edges):
        edge = list(map(int, input().split()))
        graph[edge[0]][edge[1]] = 1
        graph[edge[1]][edge[0]] = 1
        d[edge[0]] += 1
        d[edge[1]] += 1

    k = int(input("Enter the size of the clique (k): "))
    n = int(input("Enter the number of vertices: "))

    findCliques(0, 1, k)