n, m = map(int, input().split())
board = [_ for _ in range(n)]
for i in range(n):
    board[i] = list(map(int, input().split()))

type_19 = [
    [(0, 1), (0, 2), (0, 3)],
    [(1, 0), (2, 0), (3, 0)],
    [(1, 0), (0, 1), (1, 1)],
    [(0, 1), (0, 2), (1, 2)],
    [(1, 0), (2, 0), (0, 1)],
    [(1, 0), (1, 1), (1, 2)],
    [(1, 0), (2, 0), (2, -1)],
    [(0, 1), (0, 2), (-1, 2)],
    [(0, 1), (1, 1), (2, 1)],
    [(1, 0), (0, 1), (0, 2)],
    [(1, 0), (2, 0), (2, 1)],
    [(0, 1), (1, 1), (1, 2)],
    [(1, 0), (1, -1), (2, -1)],
    [(0, -1), (1, -1), (1, -2)],
    [(1, 0), (1, 1), (2, 1)],
    [(1, 0), (2, 0), (1, 1)],
    [(0, 1), (0, 2), (1, 1)],
    [(1, 0), (2, 0), (1, -1)],
    [(0, 1), (0, 2), (-1, 1)],
]


def get_score(x, y):
    max_score = -1
    for type in type_19:
        score = board[y][x]
        for (dx, dy) in type:
            square_x = x + dx
            square_y = y + dy
            if square_x < 0 or square_y < 0 or square_x >= m or square_y >= n:
                score = 0
                break
            score += board[square_y][square_x]
        max_score = max(max_score, score)
    return max_score


result = -1
for i in range(n):
    for j in range(m):
        result = max(result, get_score(j, i))

print(result)
