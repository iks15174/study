import sys

input = sys.stdin.readline
n = int(input().strip())
lines = []
parent = [i for i in range(n)]
group_size = [1 for _ in range(n)]
total_group = n
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().strip().split())
    lines.append([x1, y1, x2, y2])


def find_root(a):
    global parent
    if a == parent[a]:
        return a
    parent[a] = find_root(parent[a])
    return parent[a]


def union(a, b):
    global parent
    ap = find_root(a)
    bp = find_root(b)
    if ap != bp:
        parent[ap] = bp
        return [bp, ap]
    return [-1, -1]


def ccw(p, q, r):
    temp = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
    if temp > 0:
        return 1
    elif temp == 0:
        return 0
    elif temp < 0:
        return -1


def crossed(a, b, c, d):
    abc = ccw(a, b, c)
    abd = ccw(a, b, d)
    cda = ccw(c, d, a)
    cdb = ccw(c, d, b)

    res1 = abc * abd
    res2 = cda * cdb
    if res1 <= 0 and res2 <= 0:
        if res1 == 0 and res2 == 0:
            if a > b:
                a, b = b, a
            if c > d:
                c, d = d, c
            if c <= b and a <= d:
                return 1
            else:
                return 0
        return 1
    return 0


for i in range(n):
    for j in range(0, i):
        if crossed(lines[i][0:2], lines[i][2:], lines[j][0:2], lines[j][2:]):
            new_p, old_p = union(i, j)
            if new_p >= 0:
                total_group -= 1
                group_size[new_p] += group_size[old_p]
                group_size[old_p] = 0

print(total_group)
print(max(group_size))
