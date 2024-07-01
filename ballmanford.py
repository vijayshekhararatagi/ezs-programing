g = [
    [0, 6, 4, 5, False, False],
    [False, 0, False, False, -1, False],
    [False, -2, 0, False, 3, False],
    [False, False, -2, 0, False, -1],
    [False, False, False, False, 0, 3],
    [False, False, False, False, False, 0]
]

d = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}

# Edge list initialization
e = []
for i in range(len(g)):
    for j in range(len(g[i])):
        if g[i][j] != False and g[i][j] != 0:
            e.append((i, j, g[i][j]))

print("Edges:", [(d[u], d[v], w) for u, v, w in e])

# Distance dictionary initialization
di = {i: float('inf') for i in range(len(g))}
di[0] = 0  # Assuming vertex 'A' (index 0) is the source

print("Initial distances:", di)

# Bellman-Ford algorithm
for _ in range(len(g) - 1):
    for u, v, w in e:
        if di[u] != float('inf') and di[u] + w < di[v]:
            di[v] = di[u] + w

# Check for negative weight cycles
for u, v, w in e:
    if di[u] != float('inf') and di[u] + w < di[v]:
        print("Graph contains a negative weight cycle")
        break
else:
    # If no negative weight cycle
    print("Final distances from A:", {d[i]: di[i] for i in di})
