import sys

sys.setrecursionlimit(1000001)

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
    
root = 1
visited = [False] * (n + 1)
dp = [[0] * 2 for _ in range(n + 1)]
def solve(node):
    global graph, visited, dp
    visited[node] = True
    dp[node][0] = 0
    dp[node][1] = 1
    for nnode in graph[node]:
        if not visited[nnode]:
            solve(nnode)
            dp[node][0] += dp[nnode][1]
            dp[node][1] += min(dp[nnode][1], dp[nnode][0])

solve(root)
print(min(dp[root][0], dp[root][1]))