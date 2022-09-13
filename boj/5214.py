import sys
from collections import deque

input = sys.stdin.readline
n, k, m = map(int, input().split())
node_group = [[] for _ in range(n + 1)]
group_node = [[] for _ in range(m)]
mid = 0
for _ in range(m):
    group = list(map(int, input().split()))
    for g in group:
        node_group[g].append(mid)
        group_node[mid].append(g)
    mid += 1

root = 1    
visited = [False] * (n + 1)
visited[root] = True
if root == n:
    print(1)
    sys.exit()
q = deque([[root, 1]])
while q:
    cur, dist = q.popleft()
    cgroup = node_group[cur]
    nn = []
    for cg in cgroup:
        nn.extend(group_node[cg])
    for nnode in nn:
        if nnode == n:
            print(dist + 1)
            sys.exit()
        if not visited[nnode]:
            visited[nnode] = True
            q.append([nnode, dist + 1])
            
print(-1)