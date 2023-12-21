
import numpy as np
def dijkstra(graph, source):
    n = len(graph)
    S = {source}
    D = np.full(n, float('inf'))
    D[source - 1] = 0

    for i in range(1, n):
        w = min(set(range(1, n + 1)) - S, key=lambda x: D[x - 1])
        S = S.union({w}) 
        for v in set(range(1, n + 1)) - S:
            D[v - 1] = min(D[v - 1], D[w - 1] + graph[w - 1, v - 1])
    return D
def main():
    n = int(input("Enter the number of vertices: "))
    graph = np.zeros((n, n))
    print("Enter the edge weights for the graph:")
    for i in range(n):
        for j in range(n):
            graph[i, j] = int(input(f"Edge weight between vertex {i + 1} and {j + 1}: "))
    source_vertex = 1
    shortest_distances = dijkstra(graph, source_vertex)
    print("\nGraph in matrix form:")
    print(graph)
    print(f"\nShortest distances from vertex {source_vertex}:")
    for i, distance in enumerate(shortest_distances):
        print(f"To vertex {i + 1}: {distance}")
if __name__ == "__main__":
    main()
