def solution(n, results):
    answer = 0
    edges_win = [[] for _ in range(n + 1)]
    edges_lose = [[] for _ in range(n + 1)]
    come = [0] * (n + 1)
    for s, e in results:
        edges_win[e].append(s)
        edges_lose[s].append(e)
    for node in range(1, n + 1):
        cnt_win = 0
        q = [node]
        visited = [False] * (n + 1)
        while q:
            cur = q.pop()
            for next_n in edges_win[cur]:
                if not visited[next_n]:
                    visited[next_n] = True
                    q.append(next_n)
                    cnt_win += 1
        
        cnt_lose = 0
        q = [node]
        visited = [False] * (n + 1)
        while q:
            cur = q.pop()
            for next_n in edges_lose[cur]:
                if not visited[next_n]:
                    visited[next_n] = True
                    q.append(next_n)
                    cnt_lose += 1
        if cnt_lose + cnt_win == n - 1:
            answer += 1
    return answer