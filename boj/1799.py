import math

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
is_black = [[0] * n for _ in range(n)]
toggle = 1
for i in range(n):
    line_toggle = toggle
    for j in range(n):
        is_black[i][j] = line_toggle
        line_toggle = 1 - line_toggle
    toggle = 1 - toggle
id = -1
move = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
ans = -math.inf


def solve(id, i, j, bishop, black):
    global board, n, move, ans, is_black
    if (n - i - 1) * n + (n - j) + bishop < ans:
        return
    if i == n and j == 0:
        # if ans < bishop:
        #     print("--------------")
        #     for b in board:
        #         print(b)
        ans = max(ans, bishop)
        return
    if is_black[i][j] != black:
        if j == n - 1:
            solve(id, i + 1, 0, bishop, black)
        else:
            solve(id, i, j + 1, bishop, black)
        return
    if board[i][j] <= 0:
        if j == n - 1:
            solve(id, i + 1, 0, bishop, black)
        else:
            solve(id, i, j + 1, bishop, black)
    else:
        if j == n - 1:
            solve(id, i + 1, 0, bishop, black)
        else:
            solve(id, i, j + 1, bishop, black)
        board[i][j] = id
        for m in move:
            next_r = i + m[0]
            next_c = j + m[1]
            while 0 <= next_r < n and 0 <= next_c < n:
                if board[next_r][next_c] == 1:
                    board[next_r][next_c] = id
                next_r += m[0]
                next_c += m[1]
        if j == n - 1:
            solve(id - 1, i + 1, 0, bishop + 1, black)
        else:
            solve(id - 1, i, j + 1, bishop + 1, black)
        board[i][j] = 1
        for m in move:
            next_r = i + m[0]
            next_c = j + m[1]
            while 0 <= next_r < n and 0 <= next_c < n:
                if board[next_r][next_c] == id:
                    board[next_r][next_c] = 1
                next_r += m[0]
                next_c += m[1]


solve(id, 0, 0, 0, 0)
ans1 = ans
ans = -math.inf
solve(id, 0, 0, 0, 1)
print(ans1 + ans)
