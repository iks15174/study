import math

n, m = map(int, input().split())
memorys = list(map(int, input().split()))
costs = list(map(int, input().split()))
# dp[i] 는 i memory를 만들 수 있는 최소한의 비용이다.
dp = [math.inf] * (m + 1)
dp[0] = 0
for i in range(n):
    if memorys[i] >= m:
        dp[m] = min(dp[m], costs[i])
        continue
    for j in range(m, memorys[i] - 1, -1):
        dp[j] = min(dp[j], dp[j - memorys[i]] + costs[i])
    for j in range(memorys[i] - 1):
        dp[j] = min(dp[j], costs[i])
print(dp[m])
