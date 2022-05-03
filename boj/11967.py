n, m = map(int, input().split())
board = [[0] * n for _ in range(n)]
light = [[[] for _ in range(n)] for _ in range(n)]  # i,j에서 불을 킬 수 있는 위치를 담고있다.
move = [[0, 1], [0, -1], [1, 0], [-1, 0]]

for _ in range(m):
    i, j, x, y = map(int, input().split())
    light[i - 1][j - 1].append((x - 1, y - 1))

board[0][0] = 1
visited = [[False] * n for _ in range(n)]
q = [(0, 0)]
visited[0][0] = True


def check_around(cur_row, cur_col):  # 주위에 방문한 곳이 있는지 확인한다.
    global visited, move
    for m in move:
        next_row = cur_row + m[0]
        next_col = cur_col + m[1]
        if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
            continue
        if visited[next_row][next_col]:
            return True
    return False


while q:
    cur_row, cur_col = q.pop()
    light_switch = light[cur_row][cur_col]
    for l in light_switch:
        board[l[0]][l[1]] = 1  # 불을 밝힌다.
        if not visited[l[0]][l[1]] and check_around(l[0], l[1]):
            visited[l[0]][l[1]] = True
            q.append((l[0], l[1]))

    for m in move:
        next_row = cur_row + m[0]
        next_col = cur_col + m[1]
        if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
            continue
        if not visited[next_row][next_col] and board[next_row][next_col] == 1:
            visited[next_row][next_col] = True
            q.append((next_row, next_col))

ans = 0
for b in board:
    ans += b.count(1)
print(ans)
