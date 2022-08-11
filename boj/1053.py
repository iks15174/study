from itertools import combinations
import math
st = list(input())
def make_pallendrom(s):
    dp = [[0] * len(s) for _ in range(len(s))]
    for i in range(0, len(s) - 1, 1):
        if s[i] != s[i + 1]:
            dp[i][i + 1] = 1
            
    for inter in range(2, len(s), 1):
        for start in range(0, len(s) - inter, 1):
            end = start + inter
            cand = 0
            if s[start] == s[end]:
                cand = dp[start + 1][end - 1]
            else:
                cand = dp[start + 1][end - 1] + 1 #문자열을 교환해서 만들기
            cand = min(cand, dp[start + 1][end] + 1)
            cand = min(cand, dp[start][end - 1] + 1) #문자열 삭제 or 추가후 만들기
            dp[start][end] = cand
    return dp[0][len(s) - 1]

ans = math.inf
for ch1, ch2 in combinations(range(len(st)), 2):
    temp_st = st[:]
    temp_st[ch1] = st[ch2]
    temp_st[ch2] = st[ch1]
    ans = min(ans, make_pallendrom(temp_st) + 1)
    
print(min(ans, make_pallendrom(st)))
    