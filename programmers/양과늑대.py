# dp = []
# infog = []
# edgeg = []
# def solve(state):
#     global dp, infog, edgeg
#     if dp[state] != -1:
#         return dp[state]
    
#     temp_state = state
#     visited_node = []
#     cur_node = 0
#     wolf_num = 0
#     sheep_num = 0
#     while temp_state > 1:
#         if temp_state & 1:
#             visited_node.append(cur_node)
#         cur_node += 1
#         temp_state = temp_state >> 1
#     for v in visited_node:
#         if infog[v] == 0:
#             sheep_num += 1
#         else:
#             wolf_num += 1
#     sheep_wolf_diff = sheep_num - wolf_num
#     ans = 0
#     for v in visited_node:
#         v_connect = edgeg[v]
#         for vc in v_connect:
#             if vc not in visited_node:
#                 if sheep_wolf_diff - infog[vc] <= 0:
#                     continue
#                 ans = max(ans, solve(state | 1 << vc) + 1 - infog[vc])
#         dp[state] = ans
#         return dp[state]
# def solution(info, edges):
#     global dp, infog, edgeg
#     infog = info
#     noden = len(info)
#     edgeg = [[] for _ in range(noden)]
#     dp = [-1] * (1 << (noden + 1))
#     for s, e in edges:
#         edgeg[s].append(e)
#         edgeg[e].append(s)
#     answer = solve((1 << noden) | 1) + 1 
#     return answer


graph = []
infos = []
ans = -1
def solve(visit_record):
    global graph, infos, ans
    sheep_num = 0
    wolf_num = 0
    for vr in visit_record:
        sheep_num += 1 - infos[vr]
        wolf_num += infos[vr]
    
    is_wolf_possible = True if sheep_num - wolf_num > 1 else False 
    cand = []
    for vr in visit_record:
        for node in graph[vr]:
            if node not in visit_record and (infos[node] == 0 or is_wolf_possible):
                cand.append(node)
    if len(cand) == 0:
        sheep_cnt = 0
        for vr in visit_record:
            sheep_cnt += 1 - infos[vr]
        ans = max(ans, sheep_cnt)
        return
        
    for c in cand:
        sheep_num += 1 - infos[c]
        wolf_num += infos[c]
        if wolf_num < sheep_num:
            visit_record.add(c)
            solve(visit_record)
            visit_record.remove(c)
        sheep_num -= 1 - infos[c]
        wolf_num -= infos[c]
        
def solution(info, edges):
    global graph, infos, ans
    n = len(info)
    infos = info
    graph = [[] for _ in range(n)]
    for s, e in edges:
        graph[s].append(e)
        graph[e].append(s)
    solve(set([0]))
    return ans
    

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))