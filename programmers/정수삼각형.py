def solution(triangle):
    tri_len = len(triangle)
    dp = [[] for _ in range(tri_len)]
    dp[tri_len - 1] = triangle[-1]
    for h in range(tri_len - 2, -1, -1):
        row_len = h + 1
        for r in range(row_len):
            dp[h].append(max(dp[h + 1][r], dp[h + 1][r + 1]) + triangle[h][r])
    return dp[0][0]
