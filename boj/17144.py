r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
air_con_pos = []
for i in range(r):
    for j in range(c):
        if board[i][j] == -1:
            air_con_pos.append([i, j])


def spread_dust():
    global r, c, board, air_con_pos
    move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    new_board = [[0] * c for _ in range(r)]
    for p in air_con_pos:
        new_board[p[0]][p[1]] = -1
    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                dust = board[i][j] // 5
                cunsumed_dust = 0
                for m in move:
                    next_r = i + m[0]
                    next_c = j + m[1]
                    if (
                        next_r < 0
                        or next_r >= r
                        or next_c < 0
                        or next_c >= c
                        or board[next_r][next_c] == -1
                    ):
                        continue
                    new_board[next_r][next_c] += dust
                    cunsumed_dust += dust
                left_dust = board[i][j] - cunsumed_dust
                new_board[i][j] += left_dust
    board = new_board


def work_air_con():
    global r, c, board, air_con_pos
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for idx, p in enumerate(air_con_pos):
        px = p[0]
        py = p[1]
        x = p[0] + move[idx][0]
        y = p[1] + move[idx][1]
        d = idx
        while True:
            if x == p[0] and y == p[1]:
                break
            if board[px][py] == -1:
                board[x][y] = 0
            else:
                board[px][py] = board[x][y]
                board[x][y] = 0
            if idx == 0:
                if x == 0 and y == 0:
                    d = 3
                elif x == 0 and y == c - 1:
                    d = 1
                elif x == p[0] and y == c - 1:
                    d = 2
            if idx == 1:
                if x == r - 1 and y == 0:
                    d = 3
                elif x == r - 1 and y == c - 1:
                    d = 0
                elif x == p[0] and y == c - 1:
                    d = 2
            px = x
            py = y
            x = x + move[d][0]
            y = y + move[d][1]


for _ in range(t):
    spread_dust()
    work_air_con()

ans = 0
for b in board:
    ans += sum(b)
print(ans + 2)
