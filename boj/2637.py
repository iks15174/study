import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
dp = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, k = map(int, input().split())
    graph[x].append([y, k])
    indegree[x] += 1
complete = n

def solve(node):
    global indegree, graph, dp
    if len(dp[node]) != 0:
        return dp[node]
    temp_arr = [0] * (n + 1)
    if indegree[node] == 0:
        temp_arr[node] = 1
        dp[node] = temp_arr
        return dp[node]
    for child, w in graph[node]:
        sub_items = [si * w for si in solve(child)]
        temp_arr = [t + si for t, si in zip(temp_arr, sub_items)]
        dp[node] = temp_arr
    return dp[node]
solve(complete)
for i in range(1, n + 1):
    if indegree[i] == 0:
        print(i, dp[complete][i])