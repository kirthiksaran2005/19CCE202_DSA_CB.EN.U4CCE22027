class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = []

    def add_edge(self, start_vertex, end_vertex, weight):
        self.edges.append((start_vertex, end_vertex, weight))

    def bellman_ford(self, source_vertex):
        # Step 1: Initialize distances and predecessors
        distances = {vertex: float('inf') for vertex in range(self.num_vertices)}
        predecessors = {vertex: None for vertex in range(self.num_vertices)}
        distances[source_vertex] = 0

        # Step 2: Relax edges repeatedly
        for _ in range(self.num_vertices - 1):
            for start, end, weight in self.edges:
                if distances[start] + weight < distances[end]:
                    distances[end] = distances[start] + weight
                    predecessors[end] = start

        # Step 3: Check for negative cycles
        for start, end, weight in self.edges:
            if distances[start] + weight < distances[end]:
                raise ValueError("Graph contains a negative cycle")

        return distances, predecessors


# Example usage:
graph = Graph(5)
graph.add_edge(0, 1, 6)
graph.add_edge(0, 3, 7)
graph.add_edge(1, 2, 5)
graph.add_edge(1, 3, 8)
graph.add_edge(1, 4, -4)
graph.add_edge(2, 1, -2)
graph.add_edge(3, 2, -3)
graph.add_edge(3, 4, 9)
graph.add_edge(4, 0, 2)
graph.add_edge(4, 2, 7)

source_vertex = 4
distances, predecessors = graph.bellman_ford(source_vertex)

print(f"Shortest distances from source vertex {source_vertex}:")
for vertex in range(graph.num_vertices):
    print(f"Vertex {vertex}: Distance = {distances[vertex]}, Predecessor = {predecessors[vertex]}")
