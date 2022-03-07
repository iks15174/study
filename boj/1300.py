### 다시 풀어볼것
n = int(input())
k = int(input())
result = 0
left = 1
right = n * n
while left <= right:
    mid = (left + right) // 2
    smaller_num = 0
    for i in range(1, n + 1):
        smaller_num += min(mid // i, n)

    if smaller_num >= k:
        right = mid - 1
    else:
        left = mid + 1

print(left)
