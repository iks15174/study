row, col = map(int, input().split())
board = [list(str(input())) for _ in range(row)]
board_id = [[-1] * col for _ in range(row)]
visited = [[False] * col for _ in range(row)]
ans = 0
block_id = 0


def dfs(r, c, block_id):
    global visited, board
    q = [(r, c)]
    visited[r][c] = True
    board_id[r][c] = block_id
    connected = False
    while q:
        cr, cc = q.pop()
        nr = cr
        nc = cc
        if board[cr][cc] == "D":
            nr += 1
        elif board[cr][cc] == "U":
            nr -= 1
        elif board[cr][cc] == "R":
            nc += 1
        elif board[cr][cc] == "L":
            nc -= 1

        if not visited[nr][nc]:
            visited[nr][nc] = True
            board_id[nr][nc] = block_id
            q.append((nr, nc))

        if visited[nr][nc] and board_id[nr][nc] != block_id and board_id[nr][nc] != -1:
            connected = True

    return connected


for r in range(row):
    for c in range(col):
        if not visited[r][c]:
            if not dfs(r, c, block_id):
                ans += 1
            block_id += 1

print(ans)
