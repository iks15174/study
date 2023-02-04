def get_rank(score_sums, target):
    ans = 1
    for ss in score_sums:
        if ss > target:
            ans += 1
    return ans
        

def solution(scores):
    wanho_score = [scores[0][0], scores[0][1]]
    scores = sorted(scores, key = lambda x : (-x[0], x[1]))
    incentive_man = []
    
    pr_max = -1
    for wa, pr in scores:
        if pr < pr_max:
            if [wa, pr] == wanho_score:
                return -1
            continue
        else:
            incentive_man.append([wa, pr])
            pr_max = pr
    return get_rank(list(map(lambda x : x[0] + x[1], incentive_man)), wanho_score[0] + wanho_score[1])