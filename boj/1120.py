import math

a, b = map(list, input().split())
ans = math.inf
for i in range(len(b) - len(a) + 1):
    temp = b[i : i + len(a)]
    diff = 0
    for j in range(len(a)):
        if a[j] != temp[j]:
            diff += 1

    ans = min(ans, diff)

print(ans)
