import sys


input = sys.stdin.readline
n, m, k = map(int, input().strip().split())
minsu = sorted(list(map(int, input().strip().split())))
chulsu = list(map(int, input().strip().split()))
used = [False] * (n + 1)
parents = [i for i in range(len(minsu))]


def find(idx):
    global parents
    if idx == parents[idx]:
        return idx
    parents[idx] = find(parents[idx])
    return parents[idx]


def union(idx1, idx2):
    global m
    if idx2 >= m:
        return
    p1 = find(idx1)
    p2 = find(idx2)
    if p1 > p2:
        parents[p2] = p1
    else:
        parents[p1] = p2


def find_card(num):
    global minsu, used
    left = 0
    right = len(minsu)
    while left < right:
        mid = (left + right) // 2
        if minsu[mid] > num:
            right = mid
        else:
            left = mid + 1
    return right


for c in chulsu:
    card = find_card(c)
    real_card = find(card)
    print(minsu[real_card])
    union(real_card, real_card + 1)
