# 시간 측정이 조금 이상한 듯, 혹은 내가 효율적인 코드를 못 짜는 듯
def solution(e, starts):
    factor_count = [1] * (e + 1)
    for i in range(2, e + 1):
        for j in range(i, e + 1, i):
            factor_count[j] += 1
    
    max_num = 0
    for index in range(e, 0, -1):
        if factor_count[index] >= max_num:
            max_num = factor_count[index]
            factor_count[index] = index
        else:
            factor_count[index] = factor_count[index + 1]
        
    return [factor_count[s] for s in starts]