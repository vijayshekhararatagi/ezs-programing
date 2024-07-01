import sys

def prim_adjacency_matrix(graph):
    num_vertices = len(graph)
    selected = [False] * num_vertices
    mst_edges = []
    min_edge = [sys.maxsize] * num_vertices
    min_edge[0] = 0
    parent = [-1] * num_vertices

    for _ in range(num_vertices):
        u = min((i for i in range(num_vertices) if not selected[i]), key=lambda x: min_edge[x])
        selected[u] = True

        for v in range(num_vertices):
            if graph[u][v] and not selected[v] and graph[u][v] < min_edge[v]:
                min_edge[v] = graph[u][v]
                parent[v] = u

    for i in range(1, num_vertices):
        mst_edges.append((parent[i], i, graph[i][parent[i]]))

    return mst_edges

# Define the graph as an adjacency matrix
graph = [
    [0, 2, 3, 0, 0, 0],
    [2, 0, 1, 3, 5, 6],
    [3, 1, 0, 0, 2, 0],
    [0, 3, 0, 0, 4, 4],
    [0, 5, 2, 4, 0, 1],
    [0, 6, 0, 4, 1, 0]
]

# Find the MST starting from vertex 0
mst = prim_adjacency_matrix(graph)
print("Edges in the Minimum Spanning Tree (MST):")
for edge in mst:
    print(f"{chr(edge[0] + 65)} -- {chr(edge[1] + 65)} with weight {edge[2]}")
