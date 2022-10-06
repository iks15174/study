def solution(target):
    max_score = 100001
    possible_score = [[50, 1]]
    for i in range(1, 21):
        possible_score.append([i, 1])
        if i * 2 > 20:
            possible_score.append([i * 2, 0])
        if i * 3 > 20 and ((i * 3) % 2 != 0 or i * 3 > 40):
            possible_score.append([i * 3, 0])
    dp = [[] for _ in range(max(target + 1, 61))]
    for i in range(1, 21):
        dp[i] = [1, 1]
        dp[i * 2] = [1, 0]
        dp[i * 3] = [1, 0]
    dp[50] = [1, 1]
    for i in range(1, target + 1):
        temp_arr = []
        if len(dp[i]) == 0:
            for p, is_sb in possible_score:
                if i - p > 0:
                    temp_arr.append([dp[i - p][0] + 1, dp[i - p][1] + is_sb])
                    
            temp_arr = sorted(temp_arr, key = lambda x : (x[0], -x[1]))
            dp[i] = temp_arr[0]
    return dp[target]