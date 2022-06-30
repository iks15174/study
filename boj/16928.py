from collections import deque
n, m = map(int, input().split())
max_node = 100
start = 1
edge = [[] for _ in range(max_node)]
short_cut = [0] * max_node
for i in range(1, max_node):
    for j in range(1, 7):
        if i + j <= 100:
            edge[i].append(i + j)

for _ in range(m + n):
    s, e = map(int, input().split())
    short_cut[s] = e
    
def solve():
    global max_node, start, edge, short_cut
    q = deque([[start, 0]])
    visited = [False] * max_node
    visited[start] = True
    while q:
        cur, d = q.popleft()
        for e in edge[cur]:
            if e == max_node:
                return d + 1
            if not visited[e]:
                visited[e] = True
                cur_e = e
                while short_cut[cur_e] != 0:
                    cur_e = short_cut[cur_e]
                q.append([cur_e, d + 1])
                
print(solve())