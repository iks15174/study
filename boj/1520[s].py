from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)

m, n = map(int, input().split())

graph = []
for i in range(m):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dp = [[-1] * n for _ in range(m)]
# x, y에서 끝점으로 이동할 수 있는 경우의 수 반환
def dfs(x, y):

    if x == n - 1 and y == m - 1:
        return 1

    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        if graph[ny][nx] < graph[y][x]:
            dp[y][x] += dfs(nx, ny)

    return dp[y][x]


dfs(0, 0)
print(dp[0][0])
