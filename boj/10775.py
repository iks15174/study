import sys

input = sys.stdin.readline
g = int(input().strip())
p = int(input().strip())
air_planes = [i for i in range(g + 1)]
ans = 0


def find(a):
    global air_planes
    if a == air_planes[a]:
        return a
    air_planes[a] = find(air_planes[a])
    return air_planes[a]


def union(a1, a2):
    a1_root = find(a1)
    a2_root = find(a2)
    air_planes[a2_root] = a1_root


for _ in range(p):
    d = int(input().strip())
    r = find(d)
    if r == 0:
        break
    ans += 1
    union(r - 1, r)


print(ans)
