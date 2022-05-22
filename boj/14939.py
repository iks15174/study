import math
import copy

board = [list(input()) for _ in range(10)]
fline_switch = (1 << 10) - 1  # 01111111111
ans = math.inf


def change(value):
    if value == "O":
        return "#"
    else:
        return "O"


def touch_switch(pos, b):
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    b[pos[0]][pos[1]] = change(b[pos[0]][pos[1]])
    for m in move:
        next_r = pos[0] + m[0]
        next_c = pos[1] + m[1]
        if next_r < 0 or next_r >= 10 or next_c < 0 or next_c >= 10:
            continue
        b[next_r][next_c] = change(b[next_r][next_c])


def all_offed(b):
    for l in b:
        for c in l:
            if c == "O":
                return False
    return True


while fline_switch >= 0:
    click_num = 0
    cboard = copy.deepcopy(board)
    switch = fline_switch
    for i in range(10):
        if switch & 1:
            touch_switch((0, i), cboard)
            click_num += 1
        switch = switch >> 1

    for r in range(1, 10):
        for j in range(10):
            if cboard[r - 1][j] == "O":
                touch_switch((r, j), cboard)
                click_num += 1

    if all_offed(cboard):
        ans = min(ans, click_num)

    fline_switch -= 1
if ans == math.inf:
    print(-1)
else:
    print(ans)
