def bellman_ford(start, end, graph):
    paths = dict()
    edges = set()
    for key in graph:
        paths[key] = float('inf')
        for item in graph[key]:
            paths[item] = float('inf')
            edges.add((key, item))

    paths[start] = 0
    n = len(paths)
    
    i = 0
    while i < n:
        for edge in edges:
            src, tgt = edge[0], edge[1]
            paths[tgt] = min(paths[tgt], graph[src][tgt] + paths[src])
        i += 1
    return paths[end]

g = {
    "A": {"B": 6, "D": 1},
    "B": {"A": 6, "D": 2, "E": 2, "C": 5},
    "D": {"A": 1, "B": 2, "E": 1},
    "E": {"B": 2, "D": 1, "C": 5},
    "C": {"B": 5, "E": 5}
}

print(bellman_ford('A', 'C', g))