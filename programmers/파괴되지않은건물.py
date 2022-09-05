def solution(board, skill):
    row = len(board)
    col = len(board[0])
    sumb = [[0] * (col + 1) for _ in range(row + 1)]
    for t, r1, c1, r2, c2, d in skill:
        if t == 1:
            sumb[r1][c1] -= d
            sumb[r1][c2 + 1] += d
            sumb[r2 + 1][c1] += d
            sumb[r2 + 1][c2 + 1] -= d
        else:
            sumb[r1][c1] += d
            sumb[r1][c2 + 1] -= d
            sumb[r2 + 1][c1] -= d
            sumb[r2 + 1][c2 + 1] += d
            
    for r in range(row + 1):
        for c in range(1, col + 1):
            sumb[r][c] += sumb[r][c - 1]
            
    for c in range(col + 1):
        for r in range(1, row + 1):
            sumb[r][c] += sumb[r - 1][c]
            
    ans = 0
    for r in range(row):
        for c in range(col):
            if board[r][c] + sumb[r][c] >= 1:
                ans += 1
    return ans