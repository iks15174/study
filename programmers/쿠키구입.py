# import bisect
# def solution(cookie):
#     l_cookie = len(cookie)
#     dp = [[0] * l_cookie for _ in range(l_cookie)]
#     for i in range(l_cookie):
#         for j in range(i, l_cookie):
#             if i == j:
#                 dp[i][j] = cookie[i]
#             else:
#                 dp[i][j] = dp[i][j - 1] + cookie[j]
    
#     answer = 0
#     for l in range(l_cookie - 1):
#         for m in range(l, l_cookie - 1):
#             first_son = dp[l][m]
#             if cookie[m + 1] > first_son:
#                 continue
#             if dp[m + 1][l_cookie - 1] < first_son:
#                 break
#             pos = bisect.bisect_left(dp[m + 1], first_son, m + 1, l_cookie)
#             if dp[m + 1][pos] == first_son:
#                 answer = max(answer, first_son)
#     return answer


def solution(cookie):
    n = len(cookie)
    acc_cookie = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            if i == j:
                acc_cookie[i][j] = cookie[i]
            else:
                acc_cookie[i][j] = cookie[j] + acc_cookie[0][j - 1]
                if i != 0:
                   acc_cookie[i][j] -= acc_cookie[0][i - 1]
                
    ans = 0
    for i in range(n):
        for j in range(i + 1, n, 1):
            if acc_cookie[i][j] % 2 != 0:
                continue
            mid_val = acc_cookie[i][j] // 2
            if mid_val <= ans:
                continue
            left = i
            right = j
            while left <= right:
                mid = (left + right) // 2
                if acc_cookie[i][mid] == mid_val:
                    ans = max(ans, mid_val)
                    break
                elif acc_cookie[i][mid] > mid_val:
                    right = mid - 1
                else:
                    left = mid + 1
    return ans

print(solution([1,2,4,5]))