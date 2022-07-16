import heapq
def seperate_area(r, c, area, land, height, area_id, n):
    area[r][c] = area_id
    move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    q = [(r, c)]
    while q:
        cr, cc = q.pop()
        for m in move:
            nr = cr + m[0]
            nc = cc + m[1]
            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            if abs(land[cr][cc] - land[nr][nc]) <= height and area[nr][nc] == 0:
                area[nr][nc] = area_id
                q.append((nr, nc))
    
def find(a, arr):
    if a == arr[a]:
        return a
    arr[a] = find(arr[a], arr)
    return arr[a]

def union(a, b, arr):
    ap = find(a, arr)
    bp = find(b, arr)
    if ap == bp:
        return False
    arr[bp] = ap
    return True
    
def solution(land, height):
    n = len(land)
    area = [[0] * n for _ in range(n)]
    area_id = 1
    for r in range(n):
        for c in range(n):
            if area[r][c] == 0:
                seperate_area(r, c, area, land, height, area_id, n)
                area_id += 1
    
    ladder_candidate = []
    arr = [i for i in range(area_id)]
    move = [[0, 1], [1, 0]]
    for r in range(n):
        for c in range(n):
            for m in move:
                nr = r + m[0]
                nc = c + m[1]
                if nr < 0 or nr >= n or nc < 0 or nc >= n:
                    continue
                if abs(land[r][c] - land[nr][nc]) > height:
                    heapq.heappush(ladder_candidate, (abs(land[r][c] - land[nr][nc]), area[r][c], area[nr][nc]))
    connected_ladder = 0
    answer = 0
    while connected_ladder < area_id - 2:
        cost, area1, area2 = heapq.heappop(ladder_candidate)
        if union(area1, area2, arr):
            # print(area1, area2, cost)
            connected_ladder += 1
            answer += cost
    return answer