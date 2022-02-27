import sys

input = sys.stdin.readline
test_case = int(input())


def dfs(current_node):
    group = 1
    need_visited = []
    need_visited.append((current_node, group))

    while need_visited:
        node, group = need_visited.pop()
        if visited[node] == 0:
            visited[node] = group
            need_visited.extend(map(lambda node: (node, group * -1), edges[node]))
        elif visited[node] != group:
            return False
    return True


for i in range(test_case):
    result = True
    v, e = map(int, input().split())
    edges = [[] for _ in range(int(v) + 1)]
    visited = [0 for _ in range(int(v) + 1)]
    for j in range(e):
        n, m = map(int, input().split())
        edges[n].append(m)
        edges[m].append(n)

    finished = False
    for j in range(v):
        if visited[j + 1] == 0:
            if not dfs(j + 1):
                print("NO")
                finished = True
                break

    if not finished:
        print("YES")
