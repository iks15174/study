r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
ans = 0
move = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def seperated():  # 현재 두 덩이 이상으로 분리 되었는지 확인
    global ans
    mass = 0
    visited = [[False] * c for _ in range(r)]
    for row in range(r):
        for col in range(c):
            if not visited[row][col] and board[row][col] != 0:
                if mass == 1:
                    return True
                mass += 1
                q = [[row, col]]
                visited[row][col] = True
                while q:
                    cur_r, cur_c = q.pop()
                    for m in move:
                        next_r = cur_r + m[0]
                        next_c = cur_c + m[1]
                        if next_r < 0 or next_r >= r or next_c < 0 or next_c >= c:
                            continue
                        if board[next_r][next_c] != 0 and not visited[next_r][next_c]:
                            visited[next_r][next_c] = True
                            q.append([next_r, next_c])
    if mass == 0:  # 얼음이 다 녹음
        ans = 0
        return True
    return False


while not seperated():
    next_stat = []
    for row in range(r):
        for col in range(c):
            if board[row][col] != 0:
                sea = 0
                for m in move:
                    next_r = row + m[0]
                    next_c = col + m[1]
                    if next_r < 0 or next_r >= r or next_c < 0 or next_c >= c:
                        continue
                    if board[next_r][next_c] == 0:
                        sea += 1
                next_stat.append([row, col, max(0, board[row][col] - sea)])

    for ns in next_stat:
        board[ns[0]][ns[1]] = ns[2]

    ans += 1

print(ans)
