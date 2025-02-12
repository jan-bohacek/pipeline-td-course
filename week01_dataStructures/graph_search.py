graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "d": [],
    "c": ["e"],
    "e": ["f", "g"],
    "f": [],
    "g": [],
}

def dfs_iterative(graph, root):
    stack = [root]
    while len(stack) > 0:
        current = stack.pop()
        print(current)
        for i in graph[current]:
            stack.append(i)

# dfs_iterative(graph, "a")


def dfs_recursive(graph, root):
    print(root)
    for node in graph[root]:
        dfs_recursive(graph, node)

# dfs_recursive(graph, "a")



def bfs(graph, root):
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current)
        for i in graph[current]:
            queue.append(i)

bfs(graph, "a")