from collections import deque
import sys

row, col = map(int, input().split())
board = [list(input()) for _ in range(row)]
red = []
black = []
hole = []
for r in range(row):
    for c in range(col):
        if board[r][c] == "B":
            black = [r, c]
            board[r][c] = "."
        elif board[r][c] == "R":
            red = [r, c]
            board[r][c] = "."
        elif board[r][c] == "O":
            hole = [r, c]


def move_ball(cr, cc, m, board):
    dist = 0
    is_falled = False
    while board[cr][cc] == ".":
        dist += 1
        cr += m[0]
        cc += m[1]
    if board[cr][cc] == "O":
        is_falled = True
    return [dist, [cr - m[0], cc - m[1]], is_falled]


move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
q = deque([[red, black, 0]])

while q:
    rp, bp, cnt = q.popleft()
    # print(q)
    if cnt >= 10:
        continue
    for idx, m in enumerate(move):
        nrr = rp[0] + m[0]
        nrc = rp[1] + m[1]
        nbr = bp[0] + m[0]
        nbc = bp[1] + m[1]
        if (
            nrr < 0
            or nrr >= row
            or nrc < 0
            or nrc >= col
            or nbr < 0
            or nbr >= row
            or nbc < 0
            or nbc >= col
            or (board[nrr][nrc] == "#" and board[nbr][nbc] == "#")
        ):
            continue
        if (board[nrr][nrc] != "#") or (board[nbr][nbc] != "#"):
            dist, pos, fall = move_ball(rp[0], rp[1], m, board)
            bdist, bpos, bfall = move_ball(bp[0], bp[1], m, board)
            if fall and not bfall:
                print(1)
                sys.exit()
            if bfall:
                continue
            if pos == bpos:
                if dist < bdist:
                    bpos = [bpos[0] - m[0], bpos[1] - m[1]]
                if dist > bdist:
                    pos = [pos[0] - m[0], pos[1] - m[1]]
            q.append([pos, bpos, cnt + 1])

print(0)
