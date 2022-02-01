from itertools import combinations

n, m = map(int, input().split())
home = []
chicken = []
ans = 1e9
for i in range(n):
    line = list(map(int, input().split()))
    for index, l in enumerate(line):
        if l == 1:
            home.append([i, index])  # 집의 좌표를 저장
        elif l == 2:
            chicken.append([i, index])  # 치킨 집의 좌표를 저장

for chick_comb in combinations(chicken, m):
    chick_dist_sum = 0
    for [hx, hy] in home:
        chick_dist = 1e9
        for [cx, cy] in chick_comb:
            chick_dist = min(chick_dist, abs(hx - cx) + abs(hy - cy))
        chick_dist_sum += chick_dist
    ans = min(ans, chick_dist_sum)

print(ans)
