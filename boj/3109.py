from collections import deque
r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
move = [[1, 1], [0, 1], [-1, 1]]
answer = 0

def dfs(row, col, visited, board):
    global move, r, c
    q = [[row, col]]
    flag_on_record = []
    while q:
        cr, cc = q.pop()
        visited[cr][cc] = True
        flag_on_record.append([cr, cc])
        for m in move:
            nr = cr + m[0]
            nc = cc + m[1]
            if nr < 0 or nr >= r or nc < 0 or nc >= c or visited[nr][nc] or board[nr][nc] == 'x':
                continue
            if nc == c - 1:
                visited[nr][nc] = True
                return True
            q.append([nr, nc])
    for fr, fc in flag_on_record:
        visited[fr][fc] = False
    return False

for rr in range(r):
    if dfs(rr, 0, visited, board):
        answer += 1
print(answer)