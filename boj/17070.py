n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
move = [[0, 1], [1, 0], [1, 1]]
q = [[0, 1, 0]]  # 위치 r,c와 state 의미
ans = 0
while q:
    r, c, s = q.pop()
    for i in range(3):
        if i + s == 1:
            continue
        nr = r + move[i][0]
        nc = c + move[i][1]
        if nr < 0 or nr >= n or nc < 0 or nc >= n or board[nr][nc]:
            continue
        if i == 2 and (board[nr][nc - 1] or board[nr - 1][nc]):
            continue
        if nr == n - 1 and nc == n - 1:
            ans += 1
            continue
        q.append([nr, nc, i])

print(ans)
