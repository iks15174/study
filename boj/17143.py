# 낚시꾼이 상어를 잡고 그 다음 상어가 움직인다.
r, c, m = map(int, input().split())
shark_info = []  # 상어의 위치 r, c,  상어의 속력, 방향, 크기 정보들의 배열이다.
shark_removed = [False] * m
for _ in range(m):
    shark_info.append(list(map(int, input().split())))

move = [[0, 0], [-1, 0], [1, 0], [0, 1], [0, -1]]
ans = 0


def shark_move(cur_r, cur_c, v, dir):
    global r, c, move
    if dir <= 2:  # 위, 아래의 경우
        v = v % ((r - 1) * 2)
    else:
        v = v % ((c - 1) * 2)
    for _ in range(v):
        if dir == 1 and cur_r == 1:
            dir = 2
        elif dir == 2 and cur_r == r:
            dir = 1
        elif dir == 3 and cur_c == c:
            dir = 4
        elif dir == 4 and cur_c == 1:
            dir = 3
        cur_r += move[dir][0]
        cur_c += move[dir][1]

    return (cur_r, cur_c, dir)


def catch_fish(fisher_pos):
    global shark_info, ans, r
    min_row = r + 3
    remove_idx = -1
    for idx, shark in enumerate(shark_info):
        if not shark_removed[idx] and fisher_pos == shark[1]:
            if shark[0] < min_row:
                min_row = shark[0]
                remove_idx = idx

    if remove_idx == -1:
        return
    ans += shark_info[remove_idx][4]
    shark_removed[remove_idx] = True


fisher_pos = 1
for _ in range(c):
    shark_pos = [[-1] * (c + 1) for _ in range(r + 1)]
    catch_fish(fisher_pos)
    for idx, shark in enumerate(shark_info):
        if not shark_removed[idx]:
            new_r, new_c, new_dir = shark_move(shark[0], shark[1], shark[2], shark[3])
            shark[0] = new_r
            shark[1] = new_c
            shark[3] = new_dir
            if shark_pos[new_r][new_c] == -1:
                shark_pos[new_r][new_c] = idx
            else:
                old_idx = shark_pos[new_r][new_c]
                if shark_info[old_idx][4] > shark_info[idx][4]:
                    shark_removed[idx] = True
                else:
                    shark_pos[new_r][new_c] = idx
                    shark_removed[old_idx] = True

    fisher_pos += 1

print(ans)
