import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
v, e = map(int, input().strip().split())
node_set = [i for i in range(v + 1)]
edges = []
for _ in range(e):
    edges.append(list(map(int, input().strip().split())))

edges = sorted(edges, key=lambda i: i[2])


def find_root(node1):
    if node1 == node_set[node1]:
        return node1
    node_set[node1] = find_root(node_set[node1])
    return node_set[node1]


def union(node1, node2):
    node1_root = find_root(node1)
    node2_root = find_root(node2)
    if node1_root == node2_root:
        return False
    node_set[node2_root] = node1_root
    return True


edges_cnt = 0
ans = 0
for e in edges:
    if union(e[0], e[1]):
        edges_cnt += 1
        ans += e[2]
        if edges_cnt == v - 1:
            break

print(ans)
