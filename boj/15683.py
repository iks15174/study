import math

row, col = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]
cctvs = []
ans = math.inf
move = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def draw_cctv_area(start_r, start_c, dir):  # cctv 감시구역을 그리고, 그린 영역을 리스트로 반환한다.
    dir_val = move[dir]
    result = []
    r = start_r
    c = start_c
    while r >= 0 and r < row and c >= 0 and c < col:
        if board[r][c] == "#":
            r = r + dir_val[0]
            c = c + dir_val[1]
        elif 1 <= board[r][c] <= 5:
            r = r + dir_val[0]
            c = c + dir_val[1]
        elif board[r][c] == 6:
            break
        elif board[r][c] == 0:
            board[r][c] = "#"
            result.append((r, c))
            r = r + dir_val[0]
            c = c + dir_val[1]
    return result


for r in range(row):
    for c in range(col):
        if 1 <= board[r][c] <= 5:  # cctv와 방향의 조합이다. 0,1,2,3은 상우하좌를 나타낸다.
            if board[r][c] == 1:
                temp = []
                temp.append((board[r][c], r, c, 0))
                temp.append((board[r][c], r, c, 1))
                temp.append((board[r][c], r, c, 2))
                temp.append((board[r][c], r, c, 3))
                cctvs.append(temp)
            elif board[r][c] == 2:
                temp = []
                temp.append((board[r][c], r, c, 0))
                temp.append((board[r][c], r, c, 1))
                cctvs.append(temp)
            if board[r][c] == 3:
                temp = []
                temp.append((board[r][c], r, c, 0))
                temp.append((board[r][c], r, c, 1))
                temp.append((board[r][c], r, c, 2))
                temp.append((board[r][c], r, c, 3))
                cctvs.append(temp)
            if board[r][c] == 4:
                temp = []
                temp.append((board[r][c], r, c, 0))
                temp.append((board[r][c], r, c, 1))
                temp.append((board[r][c], r, c, 2))
                temp.append((board[r][c], r, c, 3))
                cctvs.append(temp)
            if board[r][c] == 5:
                temp = []
                temp.append((board[r][c], r, c, 0))
                cctvs.append(temp)

cctv_num = len(cctvs)  # cctv의 갯수이다.


def solve(idx):
    global ans
    if idx == cctv_num:
        sum = 0
        for r in range(row):
            for c in range(col):
                if board[r][c] == 0:
                    sum += 1
        ans = min(ans, sum)
        return

    selected_cctvs = cctvs[idx]
    for sel_cctv in selected_cctvs:
        draw_area = []
        if sel_cctv[0] == 1:
            draw_area.extend(draw_cctv_area(sel_cctv[1], sel_cctv[2], sel_cctv[3]))
        elif sel_cctv[0] == 2:
            draw_area.extend(draw_cctv_area(sel_cctv[1], sel_cctv[2], sel_cctv[3]))
            draw_area.extend(
                draw_cctv_area(sel_cctv[1], sel_cctv[2], (sel_cctv[3] + 2) % 4)
            )
        elif sel_cctv[0] == 3:
            draw_area.extend(draw_cctv_area(sel_cctv[1], sel_cctv[2], sel_cctv[3]))
            draw_area.extend(
                draw_cctv_area(sel_cctv[1], sel_cctv[2], (sel_cctv[3] + 1) % 4)
            )
        elif sel_cctv[0] == 4:
            draw_area.extend(draw_cctv_area(sel_cctv[1], sel_cctv[2], sel_cctv[3]))
            draw_area.extend(
                draw_cctv_area(sel_cctv[1], sel_cctv[2], (sel_cctv[3] + 1) % 4)
            )
            draw_area.extend(
                draw_cctv_area(sel_cctv[1], sel_cctv[2], (sel_cctv[3] + 2) % 4)
            )
        elif sel_cctv[0] == 5:
            draw_area.extend(draw_cctv_area(sel_cctv[1], sel_cctv[2], sel_cctv[3]))
            draw_area.extend(
                draw_cctv_area(sel_cctv[1], sel_cctv[2], (sel_cctv[3] + 1) % 4)
            )
            draw_area.extend(
                draw_cctv_area(sel_cctv[1], sel_cctv[2], (sel_cctv[3] + 2) % 4)
            )
            draw_area.extend(
                draw_cctv_area(sel_cctv[1], sel_cctv[2], (sel_cctv[3] + 3) % 4)
            )

        solve(idx + 1)
        for restore in draw_area:
            restore_r = restore[0]
            restore_c = restore[1]
            board[restore_r][restore_c] = 0


solve(0)
print(ans)
