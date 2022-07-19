def check_failed(r, c, board):
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    row_len = len(board)
    col_len = len(board[0])
    if board[r][c] == 0:
        return True
    for m in move:
        nr = r + m[0]
        nc = c + m[1]
        if nr < 0 or nr >= row_len or nc < 0 or nc >= col_len:
            continue
        if board[nr][nc] == 1:
            return False
    return True

def solve(cr, cc, nr, nc, board):
    if check_failed(cr, cc, board):
        return 0
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    row_len = len(board)
    col_len = len(board[0])
    win_move = 50
    lose_move = -1
    for m in move:
        ncr = cr + m[0]
        ncc = cc + m[1]
        if ncr < 0 or ncr >= row_len or ncc < 0 or ncc >= col_len or board[ncr][ncc] == 0:
            continue
        board[cr][cc] = 0
        optimistic_move = solve(nr, nc, ncr, ncc, board)
        if optimistic_move % 2 == 1:
            lose_move = max(lose_move, optimistic_move)
        else:
            win_move = min(win_move, optimistic_move)
        board[cr][cc] = 1
    if win_move != 50:
        return win_move + 1
    return lose_move + 1
    
        
        
def solution(board, aloc, bloc):
    return solve(aloc[0], aloc[1], bloc[0], bloc[1], board)