import sys


input = sys.stdin.readline
n, m, k = map(int, input().strip().split())
minsu = sorted(list(map(int, input().strip().split())))
chulsu = list(map(int, input().strip().split()))
used = [False] * (n + 1)


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
    if not used[card]:
        print(minsu[card])
        used[card] = True
    else:
        while used[card]:
            card += 1
        print(minsu[card])
        used[card] = True
