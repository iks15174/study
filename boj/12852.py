import math

n = int(input())
dp = [math.inf] * (n + 1)  # i -> 1 까지 만드는 최소 횟수
dp[1] = 0
for i in range(2, n + 1):
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    dp[i] = min(dp[i], dp[i - 1] + 1)
print(dp[n])

num_seq = n
result_list = []
while n != 1:
    result_list.append(n)
    if n % 3 == 0 and dp[n] == dp[n // 3] + 1:
        n = n // 3
    elif n % 2 == 0 and dp[n] == dp[n // 2] + 1:
        n = n // 2
    elif n - 1 > 0 and dp[n] == dp[n - 1] + 1:
        n = n - 1
result_list.append(n)
print(*result_list)
