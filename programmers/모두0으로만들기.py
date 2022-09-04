import sys
import math

sys.setrecursionlimit(10 ** 7)
def get_answer(root, graph, visited, a):
    op_cnt = 0
    is_leaf = True
    for nn in graph[root]:
        if not visited[nn]:
            is_leaf = False
            visited[nn] = True
            sub_op_cnt = get_answer(nn, graph, visited, a)
            op_cnt += (sub_op_cnt + abs(a[nn]))
            a[root] += a[nn]
            a[nn] = 0
            
    if is_leaf:
        return 0
    else:
        return op_cnt
            
def solution(a, edges):
    n = len(a)
    graph = [[] for _ in range(n)]
    for s, e in edges:
        graph[s].append(e)
        graph[e].append(s)
        
    cur_idx = 0
    cur_val = 0
    for idx, val in enumerate(a):
        if abs(val) > cur_val:
            cur_val = abs(val)
            cur_idx = idx
    ans = get_answer(cur_idx, graph, [False] * n, a)
    if a[cur_idx] == 0:
        return ans
    return -1
