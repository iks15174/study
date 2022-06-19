x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
a = [x1, y1]
b = [x2, y2]
c = [x3, y3]
d = [x4, y4]


def ccw(p, q, r):
    temp = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
    if temp > 0:
        return 1
    elif temp == 0:
        return 0
    elif temp < 0:
        return -1


def solve(a, b, c, d):
    abc = ccw(a, b, c)
    abd = ccw(a, b, d)
    cda = ccw(c, d, a)
    cdb = ccw(c, d, b)

    res1 = abc * abd
    res2 = cda * cdb
    if res1 <= 0 and res2 <= 0:
        if res1 == 0 and res2 == 0:
            if a[0] > b[0] or (a[0] == b[0] and a[1] > b[1]):
                a, b = b, a
            if c[0] > d[0] or (c[0] == d[0] and c[1] > d[1]):
                c, d = d, c
            if (c[0] < b[0] or (c[0] == b[0] and c[1] <= b[1])) and (
                a[0] < d[0] or (a[0] == d[0] and a[1] <= d[1])
            ):
                return 1
            else:
                return 0
        return 1
    return 0


print(solve(a, b, c, d))
