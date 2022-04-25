import math

n = int(input())
color_cost = [list(map(int, input().split())) for _ in range(n)]
# dp[n][i] 는 n번째 집을 i 색으로 칠했을 때 1 ~ n 까지 칠하는 최소 비용이다.

ans = math.inf


def get_dp():
    global dp, color_cost
    for i in range(1, n):
        for j in range(3):
            dp[i][j] = min(
                dp[i - 1][(j + 1) % 3] + color_cost[i][j],
                dp[i - 1][(j + 2) % 3] + color_cost[i][j],
            )


dp = [[0] * 3 for _ in range(n)]  # 첫번쨰 집을 빨간색으로 칠했을 때
dp[0][0] = color_cost[0][0]
dp[0][1] = math.inf
dp[0][2] = math.inf
get_dp()
ans = min(ans, dp[n - 1][1], dp[n - 1][2])

dp = [[0] * 3 for _ in range(n)]  # 첫번쨰 집을 파란색으로 칠했을 때
dp[0][0] = math.inf
dp[0][1] = color_cost[0][1]
dp[0][2] = math.inf
get_dp()
ans = min(ans, dp[n - 1][0], dp[n - 1][2])


dp = [[0] * 3 for _ in range(n)]  # 첫번쨰 집을 초록색으로 칠했을 때
dp[0][0] = math.inf
dp[0][1] = math.inf
dp[0][2] = color_cost[0][2]
get_dp()
ans = min(ans, dp[n - 1][0], dp[n - 1][1])

print(ans)
