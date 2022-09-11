import math

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
board_dp = [[-1] * c for _ in range(r)]


def solve(cr, cc, visited):
    global board, r, c, board_dp

    if board_dp[cr][cc] != -1:
        return board_dp[cr][cc]
    move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    max_val = -1
    for m in move:
        next_r = cr + m[0] * int(board[cr][cc])
        next_c = cc + m[1] * int(board[cr][cc])
        if (
            next_r < 0
            or next_r >= r
            or next_c < 0
            or next_c >= c
            or board[next_r][next_c] == "H"
        ):
            max_val = max(max_val, 1)
            continue
        if visited[next_r][next_c]:
            board_dp[cr][cc] = math.inf
            return math.inf
        visited[next_r][next_c] = True
        max_val = max(max_val, solve(next_r, next_c, visited) + 1)
        visited[next_r][next_c] = False
    board_dp[cr][cc] = max_val
    return max_val

visited = [[False] * c for _ in range(r)]
visited[0][0] = True
ans = solve(0, 0, visited)
print(ans if ans != math.inf else -1)
