def solution(n, m, row, col, queries):
    answer = -1
    move = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    queries.reverse()
    rng = [col, col, row, row] # 좌측 col, 우측 col, 상단 row, 하단 row 의미
    limit = [m, m, n, n]
    for cmd, dx in queries:
        last_r1 = max(0, rng[2] - dx * move[cmd][0])
        last_r2 = min(n - 1, rng[3] - dx * move[cmd][0])
        last_c1 = max(0, rng[0] - dx * move[cmd][1])
        last_c2 = min(m - 1, rng[1] - dx * move[cmd][1])
        
        if rng[cmd] + move[cmd][1 - cmd//2] < 0 or rng[cmd] + move[cmd][1 - cmd//2] >= limit[cmd]:
            last_r1 = min(last_r1, rng[2])
            last_r2 = max(last_r2, rng[3])
            last_c1 = min(last_c1, rng[0])
            last_c2 = max(last_c2, rng[1])
        
        rng[0] = last_c1
        rng[1] = last_c2
        rng[2] = last_r1
        rng[3] = last_r2
        
        if rng[0] > rng[1] or rng[2] > rng[3]:
            return 0
            
    return (rng[1] - rng[0] + 1) * (rng[3] - rng[2] + 1)


def solution(n, m, row, col, queries):
    queries.reverse()
    move = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    lr, lc, rr, rc = row, col, row, col
    for cmd, dx in queries:
        prev_lr = lr - move[cmd][0] * dx
        prev_lc = lc - move[cmd][1] * dx
        prev_rr = rr - move[cmd][0] * dx
        prev_rc = rc - move[cmd][1] * dx
        
        if cmd == 0 and lc == 0:
            prev_lc = lc
        elif cmd == 1 and rc == m - 1:
            prev_rc = rc
        elif cmd == 2 and lr == 0:
            prev_lr = lr
        elif cmd == 3 and rr == n - 1:
            prev_rr = rr
        
        if prev_lc >= m or prev_rc < 0 or prev_lr >= n or prev_rr < 0:
            return 0
        
        lr = max(0, prev_lr)
        lc = max(0, prev_lc)
        rr = min(n - 1, prev_rr)
        rc = min(m - 1, prev_rc)
        
    return (rr - lr + 1) * (rc - lc + 1)