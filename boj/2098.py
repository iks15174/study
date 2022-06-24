import math

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
max_bit = 2 ** (n+1) - 1
dp = [[0] * (max_bit + 1) for _ in range(n)]
start_pos = 0

def solve(pos, state):
    global max_bit, dp, w, n, start_pos
    if state == max_bit:
        if w[pos][start_pos] == 0:
            dp[pos][state] = math.inf
        else:
            dp[pos][state] = w[pos][start_pos]
        return dp[pos][state]
    
    if dp[pos][state] != 0:
        return dp[pos][state]
    
    temp_ans = math.inf
    for i in range(n):
        bit_pos = (1 << i)
        if not (state & bit_pos) and w[pos][i] != 0:
            temp_ans = min(temp_ans, solve(i, state | bit_pos) + w[pos][i])
    dp[pos][state] = temp_ans
    return dp[pos][state]

print(solve(start_pos, (1 << n) | 1))       