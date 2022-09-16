from collections import deque

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
n = int(input())
direction = 1


def check_flying(board, cr, cc, visited):
    global r, c
    visited[cr][cc] = True
    q = deque([[cr, cc]])
    arr = [[cr, cc]]
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while q:
        curr, curc = q.popleft()
        for m in move:
            nr = curr + m[0]
            nc = curc + m[1]
            if nr < 0 or nr >= r or nc < 0 or nc >= c:
                continue
            if not visited[nr][nc] and board[nr][nc] == "x":
                visited[nr][nc] = True
                arr.append([nr, nc])
                q.append([nr, nc])
    arr = sorted(arr, key=lambda x: (x[1], -x[0]))
    prev = -1
    for ar, ac in arr:
        if ac == prev:
            continue
        if ar == r - 1 or board[ar + 1][ac] == 'x':
            return [arr, False]
        prev = ac
    return [arr, True]


def go_to_ground(board, arr):
    global r
    while True:
        for i in range(len(arr)):
            board[arr[i][0]][arr[i][1]] = '.'
            arr[i][0] += 1
            board[arr[i][0]][arr[i][1]] = 'x'
        prev = -1
        for ar, ac in arr:
            if ac == prev:
                continue
            if ar == r - 1 or board[ar + 1][ac] == 'x':
                return
            prev = ac


def throw_stick(board, d, a):
    global c
    move = [0, 1]
    cur = [r - a, 0 if d == 1 else c - 1]
    while 0 <= cur[1] < c:
        if board[cur[0]][cur[1]] == "x":
            board[cur[0]][cur[1]] = "."
            return
        cur[0] += move[0] * d
        cur[1] += move[1] * d


def move_mineral(board):
    global r, c
    visited = [[False] * c for _ in range(r)]
    for row in range(r):
        for col in range(c):
            if not visited[row][col] and board[row][col] == "x":
                arr, is_fly = check_flying(board, row, col, visited)
                if is_fly:
                    go_to_ground(board, arr)
                    return

attacks = list(map(int, input().split()))
for a in attacks:
    throw_stick(board, direction, a)
    move_mineral(board)
    direction *= -1

for b in board:
    print(''.join(b))