import heapq

n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]
q = []
org = [i for i in range(n)]

def get_dist(x1, x2, y1, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (0.5)

def find(a):
    global org
    if org[a] == a:
        return a
    org[a] = find(org[a])
    return org[a]

def union(a, b):
    global org
    a_root = find(a)
    b_root = find(b)
    if a_root == b_root:
        return False
    org[a_root] = b_root
    return True
        
for s in range(n):
    for e in range(s + 1, n):
        start = stars[s]
        end = stars[e]
        dist = get_dist(start[0], end[0], start[1], end[1])
        heapq.heappush(q, [dist, s, e])
        
ans = 0
while q:
    cdist, s, e = heapq.heappop(q)
    if union(s, e):
        ans += cdist
        
print(round(ans, 2))