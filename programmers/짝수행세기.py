from math import comb
mod  = 10 ** 7 + 19
#dp[col][odd_num] col까지 규칙에 맞게 채웠을 때 1의 갯수가 홀수인 행의 갯수가 odd_num인 경우의 수
#시간초과 나는 이유는 comb도 dp로 풀어야 할 듯
def solution(a):
    global mod
    rl = len(a)
    cl = len(a[0])
    col_one = [0] * cl
    for c in range(cl):
        for r in range(rl):
            if a[r][c] == 1:
                col_one[c] += 1
    dp = [[0] * (rl + 1) for _ in range(cl)]
    dp[0][col_one[0]] = comb(rl, col_one[0])
    for cur_col in range(1, cl):
        cur_one = col_one[cur_col]
        for prev_odd_num in range(rl + 1):
            if dp[cur_col - 1][prev_odd_num] == 0:
                continue
            for allocate_to_odd in range(min(cur_one + 1, prev_odd_num + 1)):
                allocate_to_even = cur_one - allocate_to_odd
                if allocate_to_even > rl - prev_odd_num:
                    continue
                new_odd_num = (prev_odd_num - allocate_to_odd) + allocate_to_even
                case = (comb(prev_odd_num, allocate_to_odd) * comb(rl - prev_odd_num, allocate_to_even)) % mod
                dp[cur_col][new_odd_num] += (dp[cur_col - 1][prev_odd_num] * case) % mod
    return dp[cl - 1][0] % mod