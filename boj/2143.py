target = int(input())
n_len = int(input())
n = list(map(int, input().split()))
m_len = int(input())
m = list(map(int, input().split()))
ans = 0


def upper_bound(arr, key):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == key:
            left = mid + 1
        elif arr[mid] < key:
            left = mid + 1
        elif arr[mid] > key:
            right = mid
    return right


def lower_bound(arr, key):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == key:
            right = mid
        elif arr[mid] < key:
            left = mid + 1
        elif arr[mid] > key:
            right = mid
    return right


# n의 누적합을 구한다.
# n의 누적합을 담을 배열 #i ~ j 의 합을 의미한다.
cal_sum_n = [[0] * n_len for _ in range(n_len)]
for i in range(n_len):
    cal_sum_n[i][i] = n[i]
for i in range(n_len):
    for j in range(i + 1, n_len):
        cal_sum_n[i][j] = cal_sum_n[i][j - 1] + n[j]

# m의 누적합을 구한다.
cal_sum_m = [[0] * m_len for _ in range(m_len)]
cal_sum_m_flat = []  # 누적합 1차원 배열
for i in range(m_len):
    cal_sum_m[i][i] = m[i]
for i in range(m_len):
    for j in range(i + 1, m_len):
        cal_sum_m[i][j] = cal_sum_m[i][j - 1] + m[j]

for i in range(m_len):
    for j in range(i, m_len):
        cal_sum_m_flat.append(cal_sum_m[i][j])

cal_sum_m_flat = sorted(cal_sum_m_flat)  # flat 후 정렬
for i in range(n_len):
    for j in range(i, n_len):
        diff = target - cal_sum_n[i][j]
        lower = lower_bound(cal_sum_m_flat, diff)
        upper = upper_bound(cal_sum_m_flat, diff)

        if cal_sum_m_flat[lower] != diff:
            continue
        if cal_sum_m_flat[upper] != diff:
            upper = upper - 1

        ans += (upper - lower) + 1

print(ans)
