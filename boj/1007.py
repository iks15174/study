from itertools import combinations
import math

t = int(input())
for _ in range(t):
    n = int(input())
    points = []
    total_x = 0
    total_y = 0
    for _ in range(n):
        a, b = map(int, input().split())
        points.append([a, b])
        total_x += a
        total_y += b
    ans = math.inf
    for selected in combinations(points, n // 2):
        selec_x = 0
        selec_y = 0
        for x, y in selected:
            selec_x += x
            selec_y += y
        result_x = 2 * selec_x - total_x
        result_y = 2 * selec_y - total_y
        ans = min(ans, (result_x ** 2 + result_y ** 2) ** 0.5)
    print(ans)
