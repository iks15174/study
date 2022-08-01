from collections import deque
def diff_num(str1, str2):
    num = 0
    for s1, s2 in zip(str1, str2):
        if s1 != s2:
            num += 1
    return num

def solution(begin, target, words):
    visited = [False] * len(words)
    q = deque([(begin, 0)])
    while q:
        cword, dist = q.popleft()
        if cword == target:
            return dist
        for idx, w in enumerate(words):
            if not visited[idx] and diff_num(cword, w) == 1:
                visited[idx] = True
                q.append((w, dist + 1))
    return 0