def dfs(i, visited, computers):
    visited[i] = True
    q = [i]
    while q:
        cur = q.pop()
        for idx, con in enumerate(computers[cur]):
            if idx != cur and not visited[idx] and con == 1:
                visited[idx] = True
                q.append(idx)
        
def solution(n, computers):
    answer = 0
    visited = [False] * (n)
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i, visited, computers)
    return answer