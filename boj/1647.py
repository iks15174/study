import sys

input = sys.stdin.readline
n, m = map(int, input().strip().split())
node_parent = [i for i in range(n + 1)]


def find_p(a):
    global node_parent
    if a == node_parent[a]:
        return a
    node_parent[a] = find_p(node_parent[a])
    return node_parent[a]


def union(a, b):
    global node_parent
    p1 = find_p(a)
    p2 = find_p(b)
    node_parent[p1] = p2


edge_info = []
for _ in range(m):
    a, b, c = map(int, input().strip().split())
    edge_info.append([c, a, b])

edge_info = sorted(edge_info)
connected_edge = []
for c, a, b in edge_info:
    p1 = find_p(a)
    p2 = find_p(b)
    if p1 != p2:
        union(p1, p2)
        connected_edge.append(c)
        if len(connected_edge) == n - 1:
            break

max_edge = sorted(connected_edge)[-1]
print(sum(connected_edge) - max_edge)
