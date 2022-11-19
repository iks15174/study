def solution(routes):
    routes = sorted(routes, key = lambda x : (x[1], x[0]))
    ans = 0
    cur_camera = 50000
    for s, e in routes:
        if s <= cur_camera <= e:
            continue
        cur_camera = e
        ans += 1
    return ans