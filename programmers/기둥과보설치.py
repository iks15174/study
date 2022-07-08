board = []
PILLAR = 0
PAPER = 1


def check_pillar(r, c, n):
    global board, PILLAR, PAPER
    if r == n:
        return True
    if r + 1 <= n and PILLAR in board[r + 1][c]:
        return True
    if PAPER in board[r][c]:
        return True
    if c - 1 >= 0 and PAPER in board[r][c - 1]:
        return True
    return False


def check_paper(r, c, n):
    global board, PILLAR, PAPER
    if r + 1 <= n and PILLAR in board[r + 1][c]:
        return True
    if c + 1 <= n and r + 1 <= n and PILLAR in board[r + 1][c + 1]:
        return True
    if (
        c - 1 >= 0
        and c + 1 <= n
        and PAPER in board[r][c - 1]
        and PAPER in board[r][c + 1]
    ):
        return True
    return False


def solution(n, build_frame):
    global board, PILLAR, PAPER
    board = [[set() for _ in range(n + 1)] for _ in range(n + 1)]
    for x, y, a, b in build_frame:
        col = x
        row = n - y
        if b == 1:
            if a == PILLAR:
                if check_pillar(row, col, n):
                    board[row][col].add(PILLAR)
            else:
                if check_paper(row, col, n):
                    board[row][col].add(PAPER)
        else:
            if a == PILLAR:
                board[row][col].remove(PILLAR)
                if (
                    row - 1 >= 0
                    and PILLAR in board[row - 1][col]
                    and not check_pillar(row - 1, col, n)
                ):
                    board[row][col].add(PILLAR)
                    continue
                if row - 1 >= 0 and PAPER in board[row - 1][col] and not check_paper(row - 1, col, n):
                    board[row][col].add(PILLAR)
                    continue
                if (
                    col - 1 >= 0
                    and row - 1 >= 0
                    and PAPER in board[row - 1][col - 1]
                    and not check_paper(row - 1, col - 1, n)
                ):
                    board[row][col].add(PILLAR)
                    continue
            else:
                board[row][col].remove(PAPER)
                if (
                    PILLAR in board[row][col]
                    and not check_pillar(row, col, n)
                ):
                    board[row][col].add(PAPER)
                    continue
                if (
                    col + 1 <= n
                    and PILLAR in board[row][col + 1]
                    and not check_pillar(row, col + 1, n)
                ):
                    board[row][col].add(PAPER)
                    continue
                if (
                    col - 1 >= 0
                    and PAPER in board[row][col - 1]
                    and not check_paper(row, col - 1, n)
                ):
                    board[row][col].add(PAPER)
                    continue
                if (
                    col + 1 <= n
                    and PAPER in board[row][col + 1]
                    and not check_paper(row, col + 1, n)
                ):
                    board[row][col].add(PAPER)
                    continue
    answer = []
    for i in range(n + 1):
        for j in range(n + 1):
            if PAPER in board[i][j]:
                answer.append([j, n - i, PAPER])
            if PILLAR in board[i][j]:
                answer.append([j, n - i, PILLAR])
    return sorted(answer)