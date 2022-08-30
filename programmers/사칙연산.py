import math
dp_max = [[-math.inf] * 201 for _ in range(201)]
dp_min = [[math.inf] * 201 for _ in range(201)]

def get_max(i, j, arr):
    global dp_max
    if i == j:
        return int(arr[i])
    if j == i + 2:
        if arr[i + 1] == "+":
            return int(arr[i]) + int(arr[j])
        else:
            return int(arr[i]) - int(arr[j])
    if dp_max[i][j] != -math.inf:
        return dp_max[i][j]
    
    temp_ans = -math.inf
    for m in range(i, j - 1, 2):
        op = arr[m + 1]
        if op == "+":
            left_val = get_max(i, m, arr)
            right_val = get_max(m + 2, j, arr)
            temp_ans = max(temp_ans, left_val + right_val)
        else:
            left_val = get_max(i, m, arr)
            right_val = get_min(m + 2, j, arr)
            temp_ans = max(temp_ans, left_val - right_val)
    dp_max[i][j] = temp_ans
    return temp_ans

def get_min(i, j, arr):
    global dp_min
    if i == j:
        dp_min[i][j] = int(arr[i])
        return int(arr[i])
    if j == i + 2:
        if arr[i + 1] == "+":
            dp_min[i][j] = int(arr[i]) + int(arr[j])
            return int(arr[i]) + int(arr[j])
        else:
            dp_min[i][j] = int(arr[i]) - int(arr[j])
            return int(arr[i]) - int(arr[j])
    if dp_min[i][j] != math.inf:
        return dp_min[i][j]
    
    temp_ans = math.inf
    for m in range(i, j - 1, 2):
        op = arr[m + 1]
        if op == "+":
            left_val = get_min(i, m, arr)
            right_val = get_min(m + 2, j, arr)
            temp_ans = min(temp_ans, left_val + right_val)
        else:
            left_val = get_min(i, m, arr)
            right_val = get_max(m + 2, j, arr)
            temp_ans = min(temp_ans, left_val - right_val)
    dp_min[i][j] = temp_ans
    return temp_ans

def solution(arr):
    return get_max(0, len(arr) - 1, arr)