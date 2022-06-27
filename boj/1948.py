import sys

input = sys.stdin.readline
n = int(input().strip())
m = int(input().strip())
road = [[] for _ in range(n)]
roadv = [[] for _ in range(n)]
dist = [0] * n
check = [False] * n
connected_node = [0] * n
for _ in range(m):
    s, e, d = map(int, input().strip().split())
    s -= 1
    e -= 1
    road[s].append([e, d])
    roadv[e].append([s, d])
    connected_node[e] += 1
start, end = map(int, input().strip().split())
start -= 1
end -= 1
max_dist = -1
def get_max_dist():
    global road, start, end, dist, connected_node
    q = [[start, 0]]
    while q:
        cur, nd = q.pop()
        for next, d in road[cur]:
            dist[next] = max(dist[next], d + nd)
            connected_node[next] -= 1
            if connected_node[next] == 0:
                q.append([next, dist[next]])
            
                
def max_dist_used_road():
    global roadv, start, end, max_dist, dist, check
    q = [[end, max_dist]]
    check[end] = True
    ans = 0
    while q:
        cur, d = q.pop()
        for next, nd in roadv[cur]:
            if dist[next] == d - nd:
                ans += 1
                if not check[next]:
                    q.append([next, d - nd])
                    check[next] = True
    return ans
get_max_dist()
max_dist = dist[end]
print(max_dist)
print(max_dist_used_road())