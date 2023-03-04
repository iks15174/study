def get_acc_sum(arr):
    dp = [0] * len(arr)
    for idx, val in enumerate(arr):
        if idx == 0:
            dp[idx] = val
            continue
        dp[idx] = dp[idx - 1] + val
    return dp

def get_min(arr):
    dp_min = [0] * len(arr)
    for idx, val in enumerate(arr):
        if idx == 0:
            dp_min[idx] = val
            continue
        dp_min[idx] = min(dp_min[idx - 1], val)
    return dp_min

def get_ans(acc_sum_dp, min_dp, ans):
    for idx, max_val in enumerate(acc_sum_dp):
        if min_dp[idx] < 0:
            ans = max(ans, max_val - min_dp[idx])
        else:
            ans = max(ans, max_val)
    return ans

def solution(sequence):
    ans = 0
    puls = [(1 if idx % 2 == 0 else -1) * val for idx, val in enumerate(sequence)]
    acc_sum = get_acc_sum(puls)
    ans = get_ans(acc_sum, get_min(acc_sum), ans)
    puls = [(-1 if idx % 2 == 0 else 1) * val for idx, val in enumerate(sequence)]
    acc_sum = get_acc_sum(puls)
    ans = get_ans(acc_sum, get_min(acc_sum), ans)
    return ans