# n, k = map(int, input().split())
# matrial_values = []
# for i in range(n):
#     w, v = map(int, input().split())
#     matrial_values.append([w, v])  # 무게와 가치의 쌍으로 넣어둔다.
# # dp[i][j]는 1~i-1번쨰의 물건과 j용량이 가방이 있을 때 만들 수 있는 가치의 최대이다.
# dp = [[0] * (k + 1) for _ in range(n)]


# for i, m in enumerate(matrial_values):
#     for j in range(1, k + 1):
#         if i == 0:
#             if m[0] <= j:
#                 dp[i][j] = m[1]
#         else:
#             dp[i][j] = dp[i - 1][j]
#             if m[0] <= j:
#                 dp[i][j] = max(dp[i - 1][j - m[0]] + m[1], dp[i - 1][j])

# print(dp[n - 1][k])


n, k = map(int, input().split())
matrials = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(k + 1)]
for bag_w in range(k + 1):
    if bag_w >= matrials[0][0]:
        dp[bag_w][0] = matrials[0][1]
        
for matrial_n in range(1, n):
    for bag_weight in range(k + 1):
        if bag_weight >= matrials[matrial_n][0]:
            dp[bag_weight][matrial_n] = max(dp[bag_weight][matrial_n - 1], dp[bag_weight - matrials[matrial_n][0]][matrial_n - 1] + matrials[matrial_n][1])
        else:
            dp[bag_weight][matrial_n] = max(dp[bag_weight][matrial_n], dp[bag_weight][matrial_n - 1])
print(dp[k][n - 1])
