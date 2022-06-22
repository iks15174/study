from re import L


n, m, k = map(int, input().split())
board = [[5] * n for _ in range(n)]
trees = [[[] for _ in range(n)] for _ in range(n)]
a = [[] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
for _ in range(m):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    trees[x][y].append(z)


def spring_summer():
    global n, trees, board
    for i in range(n):
        for j in range(n):
            trees[i][j] = sorted(trees[i][j])
            for idx, t in enumerate(trees[i][j]):
                if board[i][j] >= t:
                    board[i][j] -= t
                    trees[i][j][idx] += 1
                else:
                    while idx != len(trees[i][j]):
                        board[i][j] += trees[i][j].pop() // 2
                    break


def fall():
    global n, trees, board
    move = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for i in range(n):
        for j in range(n):
            for t in trees[i][j]:
                if t % 5 == 0:
                    for m in move:
                        nr = i + m[0]
                        nc = j + m[1]
                        if nr < 0 or nr >= n or nc < 0 or nc >= n:
                            continue
                        trees[nr][nc].append(1)


def winter():
    global n, board, a
    for i in range(n):
        for j in range(n):
            board[i][j] += a[i][j]


for _ in range(k):
    spring_summer()
    fall()
    winter()

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(trees[i][j])
print(ans)
