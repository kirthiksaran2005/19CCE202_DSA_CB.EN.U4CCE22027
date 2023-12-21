def bfs(graph, start_node):
    visited = {node: False for node in graph}
    queue = []
    visited[start_node] = True
    queue.append(start_node)

    while queue:
        current_node = queue.pop(0)
        print(current_node, end=" ")

        for neighbor in graph[current_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# Example Usage:
graph_example = {
    'A': ['B', 'C', 'D'],
    'B': ['A'],
    'C': ['A', 'D'],
    'D': ['A', 'C', 'E'],
    'E': ['D'],
}

start_vertex_example = 'A'
print("BFS starting from vertex", start_vertex_example)
bfs(graph_example, start_vertex_example)
print("\n")

# Test Case 1:
graph_test1 = {
    'X': ['Y', 'Z'],
    'Y': ['X', 'W'],
    'Z': ['X', 'W'],
    'W': ['Y', 'Z']
}

start_vertex_test1 = 'X'
print("BFS starting from vertex", start_vertex_test1)
bfs(graph_test1, start_vertex_test1)
print("\n")

# Test Case 2:
graph_test2 = {
    'P': ['Q', 'R'],
    'Q': ['P', 'S'],
    'R': ['P', 'S'],
    'S': ['Q', 'R']
}

start_vertex_test2 = 'P'
print("BFS starting from vertex", start_vertex_test2)
bfs(graph_test2, start_vertex_test2)
