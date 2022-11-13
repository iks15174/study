def solution(n, s):
    val = s // n
    mod = s % n
    if val == 0:
        return [-1]
    ans = [val] * n
    for i in range(mod):
        ans[i] += 1
    return sorted(ans)