import math
import sys

sys.setrecursionlimit(10 ** 5)

dp = [[math.inf] * 151 for _ in range(151)]
maxa = 150
maxc = 150

def solve(alp, cop, problems):
    global dp, maxa, maxc
    if dp[min(maxa,alp)][min(maxc,cop)] != math.inf:
        return dp[min(maxa,alp)][min(maxc,cop)]
    
    need_alp = 0
    need_cop = 0
    possible_problems = []
    for ar, cr, aw, cw, cost in problems:
        if ar > alp:
            need_alp = max(need_alp, ar - alp)
        if cr > cop:
            need_cop = max(need_cop, cr - cop)
        if ar <= alp and cr <= cop:
            possible_problems.append([ar, cr, aw, cw, cost])
            
    if need_alp == 0 and need_cop == 0:
        dp[min(maxa,alp)][min(maxc,cop)] = 0
        return 0
    
    cost = math.inf
    if need_alp > 0:
        cost = solve(alp + 1, cop, problems) + 1
    if need_cop > 0:
        cost = min(cost, solve(alp, cop + 1, problems) + 1)
    for ar, cr, aw, cw, c in possible_problems:
        if (need_alp == 0 and cw == 0) or (need_cop == 0 and aw == 0):
            continue
        cost = min(cost, solve(alp + aw, cop + cw, problems) + c)
    dp[min(maxa,alp)][min(maxc,cop)] = cost
    return cost
        
def solution(alp, cop, problems):
    solve(alp, cop, problems)
    return dp[alp][cop]