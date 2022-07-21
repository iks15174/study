from itertools import permutations
def solution(n, weak, dist):
    answer = 20
    for start in range(len(weak)):
        for dist_order in permutations(dist):
            used = 0
            visited = 0
            cur_pos = start
            for d in dist_order:
                if visited >= len(weak):
                    break
                used += 1
                start_range = weak[cur_pos]
                end_range = start_range + d 
                while visited < len(weak):
                    if start_range <= weak[cur_pos] <= end_range or start_range <= weak[cur_pos] + n <= end_range:
                        cur_pos = (cur_pos + 1) % len(weak)
                        visited += 1
                    else:
                        break
            if len(weak) <= visited:
                answer = min(answer, used)
    if answer == 20:
        return -1
    return answer