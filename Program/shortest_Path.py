from math import inf

def multistage_shortest_path(graph, source, target, k):
	# Initialize the shortest path distances
	d = [inf] * (len(graph))
	d[target] = 0

	# Loop over each stage from k-1 to 1
	for i in range(k-1, 0, -1):
		# Loop over all vertices in the current stage
		for v in range(len(graph)):
			# Skip vertices not in the current stage
			if graph[v][0] != i:
				continue
			
			# Update the shortest path distance of the current vertex
			for u in graph[v][1]:
				d[v] = min(d[v], graph[v][1][u] + d[u])

	# Return the shortest path distance from source to target
	return d

# Example graph
graph = [
	(0, {}),
	(1, {3: 2, 4: 9}),
	(1, {3: 6, 4: 3}),
	(2, {4: 1}),
	(2, {5: 4}),
	(3, {5: 7}),
	(3, {6: 2}),
	(4, {5: 1, 6: 5}),
	(4, {6: 6}),
	(5, {}),
	(5, {}),
	(6, {}),
	(6, {}),
]

# Find the shortest path from vertex 0 to vertex 12
shortest_path_distance = multistage_shortest_path(graph, 0, 12, 7)
print("Shortest path distance from vertex 0 to vertex 12:", shortest_path_distance)
