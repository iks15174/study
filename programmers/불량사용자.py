dp = []
ans = 0

def cmp_str(str1, str2):
    if len(str1) != len(str2):
        return False
    for s1, s2 in zip(str1, str2):
        if s2 == "*":
            continue
        if s1 != s2:
            return False
    return True

def solve(user_id, banned_id, ban_idx, state):
    global dp, ans
    if ban_idx == len(banned_id):
        if not dp[state]:
            ans += 1
            dp[state] = True
        return
    temp_state = state
    user_idx = 0
    while temp_state > 1:
        if temp_state & 1 == 0 and cmp_str(user_id[user_idx], banned_id[ban_idx]):
            solve(user_id, banned_id, ban_idx + 1, state | (1 << user_idx))
        temp_state = temp_state >> 1
        user_idx += 1
            
        
def solution(user_id, banned_id):
    global dp, ans
    dp = [False] * (2 ** (len(user_id) + 1))
    solve(user_id, banned_id, 0, (1 << len(user_id)))
    return ans
