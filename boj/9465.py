test = int(input())
for _ in range(test):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    if n == 1:
        print(max(sticker[0][0], sticker[1][0]))
        continue
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    dp[0][1] = sticker[0][1] + sticker[1][0]
    dp[1][1] = sticker[1][1] + sticker[0][0]
    for i in range(2, n):
        for j in range(2):
            dp[j][i] = max(dp[1 - j][i - 1], dp[1 - j][i - 2]) + sticker[j][i]
    print(max(dp[0][n - 1], dp[1][n - 1]))
