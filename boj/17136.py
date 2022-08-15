import math
board = [list(map(int, input().split())) for _ in range(10)]
paper_left = [5] * 5
ones_pos = []
answer = math.inf
for i in range(10):
    for j in range(10):
        if board[i][j] == 1:
            ones_pos.append((i, j))
            
def square_possible(i, j, length, board):
    for r in range(i, i + length):
        for c in range(j, j + length):
            if r < 0 or r >= 10 or c < 0 or c >= 10:
                return False
            if board[r][c] == 0:
                return False
    return True 

def fill_board(cr, cc, length, board, num):
    for r in range(cr, cr + length):
        for c in range(cc, cc + length):
            board[r][c] = num
            
def solve(board, paper_left, ones_pos, cnt, op_idx):
    global answer
    if len(ones_pos) == op_idx:
        answer = min(answer, cnt)
        return
    cr, cc = ones_pos[op_idx]
    if board[cr][cc] == 1:
        for length in range(1, 6):
            if square_possible(cr, cc, length, board) and paper_left[length - 1] > 0:
                fill_board(cr, cc, length, board, 0)
                paper_left[length - 1] -= 1
                solve(board, paper_left, ones_pos, cnt + 1, op_idx + 1)
                fill_board(cr, cc, length, board, 1)
                paper_left[length - 1] += 1
    else:
        solve(board, paper_left, ones_pos, cnt, op_idx + 1)

solve(board, paper_left, ones_pos, 0, 0)
print(-1 if answer == math.inf else answer)