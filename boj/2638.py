r, c = map(int, input().split())
table = [[] for _ in range(r)]
for i in range(r):
    table[i] = list(map(int, input().split()))
move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
ans = 0


def separate_space():
    q = [(0, 0)]
    table[0][0] = 2  # 치즈밖의 영역은 2로 표시
    while q:
        row, col = q.pop()
        for m in move:
            next_r = row + m[0]
            next_c = col + m[1]
            if next_r < 0 or next_r >= r or next_c < 0 or next_c >= c:
                continue
            if (
                table[next_r][next_c] == 1 or table[next_r][next_c] == 2
            ):  # 치즈이거나 방문했던 곳이면 넘긴다.
                continue
            table[next_r][next_c] = 2
            q.append((next_r, next_c))


while True:
    separate_space()  # 치즈 내 외부의 공간을 구별한다.
    delete_list = []
    for i in range(r):
        for j in range(c):
            if table[i][j] == 1:
                air_contact = 0
                for m in move:
                    next_r = i + m[0]
                    next_c = j + m[1]
                    if table[next_r][next_c] == 2:
                        air_contact += 1

                if air_contact >= 2:
                    delete_list.append((i, j))

    if len(delete_list) == 0:  # 삭제할 치즈가 없다는것은 끝났다는 것이다.
        break

    ans += 1
    for d_row, d_col in delete_list:
        table[d_row][d_col] = 0  # 치즈를 삭제한다.

    for i in range(r):
        for j in range(c):
            if table[i][j] == 2:  # 치즈 밖의 영역을 다시 0으로 되돌린다.
                table[i][j] = 0

print(ans)
