import math

def solution(beginning, target):
    ans = math.inf
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
        cnt = 0
        new_diff = [d[:] for d in diff]
        sr = selected_row
        cur_row = 0
        while sr > 0:
            if sr & 1:
                cnt += 1
                for c in range(col):
                    new_diff[cur_row][c] = 1 - new_diff[cur_row][c]
            sr = sr >> 1
            cur_row += 1
        
        for cur_c in range(col):
            temp_sum = 0
            for cur_r in range(row):
                temp_sum += new_diff[cur_r][cur_c]
            if temp_sum == 0 or temp_sum == row:
                cnt += (0 if temp_sum == 0 else 1)
            else:
                cnt += math.inf
                break
                    
        ans = min(ans, cnt)
    
    if ans == math.inf:
        return -1
    else:
        return ans