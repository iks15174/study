import sys

sys.setrecursionlimit(10 ** 6)
def solve(dp, tree, cur_node, visited):
    visited[cur_node] = True
    dp[1][cur_node] = 1
    for nnode in tree[cur_node]:
        if not visited[nnode]:
            solve(dp, tree, nnode, visited)
            dp[0][cur_node] += dp[1][nnode]
            dp[1][cur_node] += min(dp[1][nnode], dp[0][nnode])
    return
def solution(n, lighthouse):
    tree = [[] for _ in range(n)]
    for a, b in lighthouse:
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)
    root = 0
    visited = [False] * n
    dp = [[0] * n for _ in range(2)]
    solve(dp, tree, root, visited)
    return min(dp[0][root], dp[1][root])