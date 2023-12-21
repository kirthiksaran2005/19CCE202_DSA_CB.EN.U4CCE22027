import heapq

def prim(graph, start):
    mst = []  # Minimum Spanning Tree
    visited = set()
    priority_queue = [(0, start)]  # Priority queue using heapq

    while priority_queue:
        cost, current = heapq.heappop(priority_queue)

        if current not in visited:
            visited.add(current)
            mst.append((cost, current))

            for neighbor, weight in graph[current].items():
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (weight, neighbor))

    return mst

# Example Usage:
graph_example = {
    'A': {'B': 2, 'D': 5},
    'B': {'A': 2, 'D': 3, 'E': 1},
    'C': {'E': 4},
    'D': {'A': 5, 'B': 3, 'E': 1, 'F': 6},
    'E': {'B': 1, 'C': 4, 'D': 1, 'F': 7},
    'F': {'D': 6, 'E': 7}
}

start_vertex_example = 'A'
minimum_spanning_tree = prim(graph_example, start_vertex_example)

print("Minimum Spanning Tree using Prim's algorithm:")
for edge in minimum_spanning_tree:
    print(f"Edge: {edge[1]} - {edge[0]}")
