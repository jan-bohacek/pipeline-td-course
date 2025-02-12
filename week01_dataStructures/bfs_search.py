graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "d": [],
    "c": ["e"],
    "e": ["f", "g"],
    "f": [],
    "g": [],
}

def bfs_search(graph, root):
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current)
        for i in graph[current]:
            queue.append(i)

# bfs_search(graph, "a")

def dfs_recursive(graph, root):
    print(root)
    for i in graph[root]:
        dfs_recursive(graph, i)

dfs_recursive(graph, "a")
