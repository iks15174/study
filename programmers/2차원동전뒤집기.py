import math

ans = math.inf 
def update_ans(row, col, selected_row, selected_col, new_diff, one_cnt):
    global ans
    row_set = set()
    col_set = set()
    row_idx = 0
    col_idx = 0
    while selected_row > 0:
        if selected_row & 1:
            row_set.add(row_idx)
        row_idx += 1
        selected_row = selected_row >> 1
    
    while selected_col > 0:
        if selected_col & 1:
            col_set.add(col_idx)
        col_idx += 1
        selected_col = selected_col >> 1
        
    if len(col_set) + len(row_set) >= ans:
        return
    
    for r in range(row):
        for c in range(col):
            if r in row_set:
                new_diff[r][c] = (1 - new_diff[r][c])
                one_cnt += (-1 if not new_diff[r][c] else 1)
            if c in col_set:
                new_diff[r][c] = (1 - new_diff[r][c])
                one_cnt += (-1 if not new_diff[r][c] else 1)
                
    if one_cnt == 0:
        ans = min(ans, len(col_set) + len(row_set))
    
def solution(beginning, target):
    global ans
    row = len(beginning)
    col = len(beginning[0])
    diff = [[0] * col for _ in range(row)]
    one_cnt = 0
    for r in range(row):
        for c in range(col):
            if beginning[r][c] != target[r][c]:
                diff[r][c] = 1
                one_cnt += 1
                
    for selected_row in range(2 ** row):
        for selected_col in range(2 ** col):
            new_diff = [d[:] for d in diff]
            update_ans(row, col, selected_row, selected_col, new_diff, one_cnt)
    if ans == math.inf:
        return -1
    else:
        return ans