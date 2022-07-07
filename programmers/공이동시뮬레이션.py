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