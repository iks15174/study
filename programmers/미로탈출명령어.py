def is_possible(n, m, x, y, r, c, k, d):
    nr = x + d[0]
    nc = y + d[1]
    if nr <= 0 or nr > n or nc <= 0 or nc > m:
        return False
    dist = abs(nr - r) + abs(nc - c)
    if dist > k - 1:
        return False
    return True
    
def solution(n, m, x, y, r, c, k):
    distance = abs(x - r) + abs(y - c)
    if distance > k or (k - distance) % 2 == 1:
        return "impossible"
    ans = ""
    move = [[1, 0, 'd'], [0, -1, 'l'], [0, 1, 'r'], [-1, 0, 'u']]
    while k > 0:
        for d in move:
            if is_possible(n, m, x, y, r, c, k, d):
                x += d[0]
                y += d[1]
                k -= 1
                ans += d[2]
                break
    return ans