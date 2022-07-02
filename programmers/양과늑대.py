dp = []
infog = []
edgeg = []
def solve(state):
    global dp, infog, edgeg
    if dp[state] != -1:
        return dp[state]
    
    temp_state = state
    visited_node = []
    cur_node = 0
    wolf_num = 0
    sheep_num = 0
    while temp_state > 1:
        if temp_state & 1:
            visited_node.append(cur_node)
        cur_node += 1
        temp_state = temp_state >> 1
    for v in visited_node:
        if infog[v] == 0:
            sheep_num += 1
        else:
            wolf_num += 1
    sheep_wolf_diff = sheep_num - wolf_num
    ans = 0
    for v in visited_node:
        v_connect = edgeg[v]
        for vc in v_connect:
            if vc not in visited_node:
                if sheep_wolf_diff - infog[vc] <= 0:
                    continue
                ans = max(ans, solve(state | 1 << vc) + 1 - infog[vc])
        dp[state] = ans
        return dp[state]
def solution(info, edges):
    global dp, infog, edgeg
    infog = info
    noden = len(info)
    edgeg = [[] for _ in range(noden)]
    dp = [-1] * (1 << (noden + 1))
    for s, e in edges:
        edgeg[s].append(e)
        edgeg[e].append(s)
    answer = solve((1 << noden) | 1) + 1 
    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))