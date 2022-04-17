import sys

input = sys.stdin.readline
node, m = map(int, input().strip().split())
node_root = [i for i in range(node)]
sys.setrecursionlimit(10 ** 6)


def find_root(node1):
    if node_root[node1] == node1:
        return node1
    node_root[node1] = find_root(node_root[node1])
    return node_root[node1]


def union(node1, node2):
    node1_root = find_root(node1)
    node2_root = find_root(node2)
    if node1_root == node2_root:
        return True
    node_root[node2_root] = node1_root
    return False


connect_info = []
for _ in range(m):
    node1, node2 = map(int, input().strip().split())
    connect_info.append((node1, node2))

ans = 0
finished = False
for (node1, node2) in connect_info:
    ans += 1
    finished = union(node1, node2)
    if finished:
        break

if finished:
    print(ans)
else:
    print(0)
