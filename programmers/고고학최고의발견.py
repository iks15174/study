import math

ans = math.inf
dp_set = set()


def finished(clockHands, l):
    for element in clockHands[l - 1]:
        if element != 0:
            return False
    return True


def move(l, clockHands, cr, cc, num):
    mo = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    clockHands[cr][cc] = (clockHands[cr][cc] + num) % 4
    for m in mo:
        nr = cr + m[0]
        nc = cc + m[1]
        if nr < 0 or nr >= l or nc < 0 or nc >= l:
            continue
        clockHands[nr][nc] = (clockHands[nr][nc] + num) % 4


def adjust_clock(cur_row, l, clockHands, cnt):
    global ans
    if cnt >= ans:
        return
    if cur_row == l:
        if finished(clockHands, l):
            ans = min(ans, cnt)
        return
    new_cnt = cnt
    move_record = []
    for cur_col in range(l):
        up_dir = clockHands[cur_row - 1][cur_col]
        move_need = (4 - up_dir) % 4
        move_record.append(move_need)
        move(l, clockHands, cur_row, cur_col, move_need)
        new_cnt += move_need

    adjust_clock(cur_row + 1, l, clockHands, new_cnt)

    for mr, cur_col in zip(move_record, range(l)):  # 원상복귀
        move(l, clockHands, cur_row, cur_col, (4 - mr) % 4)


def solve(cur_idx, l, clockHands, cnt):
    global ans, dp_set
    if cur_idx == l:  # 첫째줄을 다 바꿨을 때
        if cnt < ans:
            state = "".join(list(map(str, clockHands[0] + clockHands[1])))
            if(state == '00000000'):
                for c in clockHands:
                    print(c)
            if state not in dp_set:
                if(state == '00000000'):
                    print('hi2')
                adjust_clock(1, l, clockHands, cnt)
                dp_set.add(state)
        return
    for i in range(1, 5):
        cur_cnt = cnt + (i % 4)
        move(l, clockHands, 0, cur_idx, 1)
        solve(cur_idx + 1, l, clockHands, cur_cnt)


def solution(clockHands):
    global ans
    solve(0, len(clockHands), clockHands, 0)
    return ans


print(
    solution(
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
)
