import bisect
def solution(cookie):
    l_cookie = len(cookie)
    dp = [[0] * l_cookie for _ in range(l_cookie)]
    for i in range(l_cookie):
        for j in range(i, l_cookie):
            if i == j:
                dp[i][j] = cookie[i]
            else:
                dp[i][j] = dp[i][j - 1] + cookie[j]
    
    answer = 0
    for l in range(l_cookie - 1):
        for m in range(l, l_cookie - 1):
            first_son = dp[l][m]
            if cookie[m + 1] > first_son:
                continue
            if dp[m + 1][l_cookie - 1] < first_son:
                break
            pos = bisect.bisect_left(dp[m + 1], first_son, m + 1, l_cookie)
            if dp[m + 1][pos] == first_son:
                answer = max(answer, first_son)
    return answer