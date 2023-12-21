def custom_dfs(visited_nodes, graph, start_node):
    if start_node not in visited_nodes:
        print(start_node)
        visited_nodes.add(start_node)
        for neighbor in graph[start_node]:
            custom_dfs(visited_nodes, graph, neighbor)

# Example Usage:
custom_graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited_set = set()

# Test Case 1
print("DFS starting from vertex '5'")
custom_dfs(visited_set, custom_graph, '5')

# Test Case 2
visited_set.clear()
print("\nDFS starting from vertex '7'")
custom_dfs(visited_set, custom_graph, '7')

# Test Case 3
visited_set.clear()
print("\nDFS starting from vertex '8'")
custom_dfs(visited_set, custom_graph, '8')
