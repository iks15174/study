'''
dp[v][0] 은 v를 root로 가지는 tree에 대해서 v가 참석하지 않을 때 tree의 모든 팀이 회의에 참석하도록 하는 가장 작은 값을 의미한다.
dp[v][1] 은 위의 정의에서 v가 참석할 경우이다.
dp는 정의에 따라 다음과 같이 정의될 수 있다.
dp[v][1]은 v의 children에 대해서 dp[c][0]과 dp[c][1] 중 작은 값을 모두 합한 값이다.
dp[v][0]을 구할 때 주의해야 하는데, dp[v][0]에 dp[c][0]만 더해진다면, v가 속한 팀이 포함되지 않기 때문에 dp 정의에 어긋난다. 그러므로
이 경우의 예외처리를 잘 해줘야 한다.
'''
import math
import sys
sys.setrecursionlimit(10 ** 7)
tree = [[] for _ in range(300000)]
dp = [[0, 0] for _ in range(300000)]
def solve(sales, node):
    global dp, tree
    if len(tree[node]) == 0:
        dp[node][0] = 0
        dp[node][1] = sales[node]
        return
    extra_cost = math.inf
    for child in tree[node]:
        solve(sales, child)
        if dp[child][0] < dp[child][1]:
            dp[node][1] += dp[child][0]
            dp[node][0] += dp[child][0]
            extra_cost = min(extra_cost, dp[child][1] - dp[child][0])
        else:
            dp[node][1] += dp[child][1]
            dp[node][0] += dp[child][1]
            extra_cost = 0
    dp[node][0] += extra_cost
    dp[node][1] += sales[node]
def solution(sales, links):
    global tree
    for s, e in links:
        tree[s - 1].append(e - 1)
    solve(sales, 0)
    return min(dp[0][0], dp[0][1])
    