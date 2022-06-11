from itertools import combinations

r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
empty_area = []
virus = []


def dfs(pos, visited):
    global board, r, c
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = [pos]
    while q:
        cur = q.pop()
        for m in move:
            nr = cur[0] + m[0]
            nc = cur[1] + m[1]
            if nr < 0 or nr >= r or nc < 0 or nc >= c:
                continue
            if board[nr][nc] == 0 and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append([nr, nc])


for i in range(r):
    for j in range(c):
        if board[i][j] == 0:
            empty_area.append([i, j])
        if board[i][j] == 2:
            virus.append([i, j])

ans = -1
for comb in combinations(empty_area, 3):
    for pos in comb:
        board[pos[0]][pos[1]] = 1

    visited = [[False] * c for _ in range(r)]
    for v in virus:
        dfs(v, visited)
    cnt = 0
    for i in range(r):
        for j in range(c):
            if board[i][j] == 0 and not visited[i][j]:
                cnt += 1
    ans = max(ans, cnt)
    for pos in comb:
        board[pos[0]][pos[1]] = 0


print(ans)
