import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
abcd = [list(map(int, input().split())) for _ in range(n)]
ab_dic = defaultdict(int)
for i in range(n):
    for j in range(n):
        val = abcd[i][0] + abcd[j][1]
        ab_dic[val] += 1
ans = 0
for i in range(n):
    for j in range(n):
        val = abcd[i][2] + abcd[j][3]
        if ab_dic.get(-val):
            ans += ab_dic[-val]
print(ans)