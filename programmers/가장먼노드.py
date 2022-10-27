from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n)]
    for s, e in edge:
        graph[s - 1].append(e - 1)
        graph[e - 1].append(s - 1)
    dist = [-1] * n
    max_val = -1
    dist[0] = 0
    q = deque([[0, 0]])
    while q:
        node, cdist = q.popleft()
        for nnode in graph[node]:
            if dist[nnode] == -1:
                dist[nnode] = cdist + 1
                max_val = max(max_val, cdist + 1)
                q.append([nnode, cdist + 1])
    return len(list(filter(lambda x : x == max_val, dist)))
