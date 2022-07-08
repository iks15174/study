import math
def solution(a):
    min_val = min(a)
    min_idx = a.index(min_val)
    answer = 0
    cur = math.inf
    for i in range(0, min_idx):
        if a[i] < cur:
            answer += 1
            cur = a[i]
    cur = math.inf
    for i in range(len(a) - 1, min_idx, -1):
        if a[i] < cur:
            answer += 1
            cur = a[i]
    return answer + 1