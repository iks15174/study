asnwer_result = []
max_score = -1
def solve(score_state, info, n):
    global max_score, answer_result
    if len(score_state) == 11:
        temp_score = 0
        apache_score = 0
        temp_result = []
        for idx, s in enumerate(score_state):
            if s:
                temp_result.append(info[idx] + 1)
                temp_score += (10 - idx)
            else:
                if info[idx] != 0:
                    apache_score += (10 - idx)
                temp_result.append(0)
        if sum(temp_result) > n:
            return
        temp_result[10] += (n - sum(temp_result))
        score_diff = temp_score - apache_score
        if score_diff <= 0:
            return
        if max_score == score_diff:
            answer_result.append(temp_result)
        elif score_diff > max_score:
            max_score = score_diff
            answer_result = [temp_result]
        return
    score_state.append(False)
    solve(score_state, info, n)
    score_state.pop()
    score_state.append(True)
    solve(score_state, info, n)
    score_state.pop()
        
def solution(n, info):
    global answer_result, max_score
    solve([], info, n)
    if max_score == -1:
        return [-1]
    print(answer_result)
    answer_result = sorted(answer_result, key= lambda x : (-x[10], -x[9], -x[8], -x[7], -x[6], -x[5], -x[4], -x[3], -x[2], -x[1], -x[0]))
    return answer_result[0]