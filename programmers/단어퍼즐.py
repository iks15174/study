def solution(strs, t):
    dp = [20002] * len(t)
    for i in range(len(t)):
        sub_t = t[0 : i + 1]
        for s in strs:
            if sub_t.endswith(s):
                dp[i] = min(dp[i], 1 if i - len(s) < 0 else dp[i - len(s)] + 1)
    if dp[-1] == 20002:
        return -1
    else:
        return dp[-1]
                