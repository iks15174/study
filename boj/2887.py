import sys
import heapq

input = sys.stdin.readline
n = int(input().strip())
planets = []
for i in range(n):
    x, y, z = map(int, input().strip().split())
    planets.append([x, y, z, i])

planets_x = sorted(planets)
planets_y = sorted(planets, key = lambda x : x[1])
planets_z = sorted(planets, key = lambda x : x[2])

ans = 0
dist_q = []
connected = 0
root = [i for i in range(n)]
for i in range(n - 1):
    heapq.heappush(dist_q, [abs(planets_x[i][0] - planets_x[i + 1][0]), planets_x[i][3], planets_x[i + 1][3]])
    heapq.heappush(dist_q, [abs(planets_y[i][1] - planets_y[i + 1][1]), planets_y[i][3], planets_y[i + 1][3]])
    heapq.heappush(dist_q, [abs(planets_z[i][2] - planets_z[i + 1][2]), planets_z[i][3], planets_z[i + 1][3]])
    
    
def find(a):
    global root
    if root[a] != a:
        root[a] = find(root[a])
    return root[a]

def union(a, b):
    global root
    a_root = find(a)
    b_root = find(b)
    if a_root != b_root:
        root[a_root] = b_root
        return True
    return False
        
while connected < n - 1:
    dist, a, b = heapq.heappop(dist_q)
    if union(a, b):
        connected += 1
        ans += dist
print(ans)
    
