import heapq

def tsp(graph):
    n = len(graph)

    vis = [0] * n
    minheap = []
    heapq.heappush(minheap, (0, 0, -1))

    mst = [[] for _ in range(n)]

    while minheap:
        wt, node, parent = heapq.heappop(minheap)

        if vis[node] == 1:
            continue

        vis[node] = 1

        if parent != -1:
            mst[node].append(parent)
            mst[parent].append(node)

        for v, w in graph[node]:
            if not vis[v]:
                heapq.heappush(minheap, (w, v, node))

    vis = [0] * n
    order = []

    def dfs(node):
        vis[node] = 1
        order.append(node)
        for i in mst[node]:
            if not vis[i]:
                dfs(i)

    dfs(0)
    order.append(0)

    cost = 0
    for i in range(len(order) - 1):
        u = order[i]
        v = order[i + 1]

        for node, wt in graph[u]:
            if node == v:
                cost += wt
                break

    return cost, order


graph = [
    [(1, 2), (2, 4), (3, 7)],
    [(0, 2), (2, 3), (3, 6)],
    [(0, 4), (1, 3), (3, 5)],
    [(0, 7), (1, 6), (2, 5)]
]

cost, route = tsp(graph)

print("Minimum approximate time:", cost)
print("Route:", route)