n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ground_id = 2  # 섬의 아이디는 2부터 시작한다.
move = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def set_ground_id(row, col):
    global board, ground_id, n
    board[row][col] = ground_id
    q = [(row, col)]
    while q:
        cur_r, cur_c = q.pop()
        for m in move:
            next_r = cur_r + m[0]
            next_c = cur_c + m[1]
            if next_c < 0 or next_c >= n or next_r < 0 or next_r >= n:
                continue
            if board[next_r][next_c] == 1:
                board[next_r][next_c] = ground_id
                q.append((next_r, next_c))


# 각 섬마다 번호 id를 줬다.
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            set_ground_id(i, j)
            ground_id += 1

ground_edge = {}  # 각 섬 별 테두리를 담고 있는 딕션너리이다.
for g in range(2, ground_id):
    ground_edge[g] = []

# 각 섬별 테두리-바다와 인접한 곳을 찾았다.
for i in range(n):
    for j in range(n):
        if 1 < board[i][j] < ground_id:
            near_sea = 0
            for m in move:
                next_r = i + m[0]
                next_c = j + m[1]

                if next_c < 0 or next_c >= n or next_r < 0 or next_r >= n:
                    continue

                if board[next_r][next_c] == 0:
                    near_sea += 1
                    break
            if near_sea != 0:
                ground_edge[board[i][j]].append((i, j))


def find_min_dist(board1, board2):
    ans = 300
    for b1r, b1c in board1:
        for b2r, b2c in board2:
            ans = min(ans, abs(b1r - b2r) + abs(b1c - b2c))
    return ans


result = 300
for g1 in range(2, ground_id):
    for g2 in range(g1 + 1, ground_id):
        result = min(result, find_min_dist(ground_edge[g1], ground_edge[g2]))

print(result - 1)
