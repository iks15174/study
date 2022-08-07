import heapq
import math
def is_reverse(target, node, cstate, traps):
    result = False
    for idx, t in enumerate(traps):
        if (t == node or t == target) and (cstate & (1 << idx)):
            result = not result
    return result
def update_state(target, cstate, traps):
    for idx, t in enumerate(traps):
        if t == target:
            return cstate ^ (1 << idx)
    return cstate
def solution(n, start, end, roads, traps):
    state_num = 2 ** (len(traps))
    distance = [[math.inf] * (n + 1) for _ in range(state_num)]
    graph = [[[] for _ in range(n + 1)] for _ in range(2)]
    for p, q, s in roads:
        graph[0][p].append((q, s))
        graph[1][q].append((p, s))
    q = []
    heapq.heappush(q, (0, start, 0)) #거리, 현재 노드, 현재 상태를 의미
    while q:
        dist, node, cstate = heapq.heappop(q)
        if node == end:
            return dist
        if distance[cstate][node] < dist:
            continue
        for target, w in graph[0][node]:
            if not is_reverse(target, node, cstate, traps):
                new_state = update_state(target, cstate, traps)
                if distance[new_state][target] > dist + w:
                    distance[new_state][target] = dist + w
                    heapq.heappush(q, (dist + w, target, new_state))
                    
        for target, w in graph[1][node]:
            if is_reverse(target, node, cstate, traps):
                new_state = update_state(target, cstate, traps)
                if distance[new_state][target] > dist + w:
                    distance[new_state][target] = dist + w
                    heapq.heappush(q, (dist + w, target, new_state))
                    
    return -1
                    
        