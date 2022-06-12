import sys

input = sys.stdin.readline
lines = int(input().strip())
connection = []
temp = []
for _ in range(lines):
    s, e = map(int, input().strip().split())
    connection.append([s, e])
connection = sorted(connection)
idxes = []
used_index = [False] * len(connection)


def find_upper(arr, val):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid][1] > val:
            right = mid
        else:
            left = mid + 1
    return right


lcs = []
result = None
for c in connection:
    if not lcs or lcs[-1][1] < c[1]:
        lcs.append(c)
        idxes.append(len(lcs) - 1)
    else:
        pos = find_upper(lcs, c[1])
        lcs[pos] = c
        idxes.append(pos)

find = len(lcs) - 1
for i in range(len(idxes) - 1, -1, -1):
    if idxes[i] == find:
        used_index[i] = True
        find -= 1
print(lines - len(lcs))
for i in range(len(used_index)):
    if not used_index[i]:
        print(connection[i][0])
