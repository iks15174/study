import math
def solution(gems):
    gems_kind = {}
    for g in gems:
        if g not in gems_kind:
            gems_kind[g] = 0
    left = 0
    right = 0
    range_len = math.inf
    range_result = []
    zero_kind = len(gems_kind)
    zero_kind -= 1
    gems_kind[gems[0]] = 1
    while True:
        if zero_kind > 0:
            right += 1
            if right == len(gems):
                break
            if gems_kind[gems[right]] == 0:
                zero_kind -= 1
            gems_kind[gems[right]] += 1
        else:
            if (right - left + 1) < range_len:
                range_len = (right - left + 1)
                range_result = [left + 1, right + 1]
            gems_kind[gems[left]] -= 1
            if gems_kind[gems[left]] == 0:
                zero_kind += 1
            left += 1
    return range_result