import sys
import math

n = int(input())
M_candidate = []
cur = 0
is_charged = False
max_limit = -1


def gcd_N(arr):
    gcd = arr[0]
    for item in arr:
        gcd = math.gcd(gcd, item)
    return gcd


for _ in range(n):
    move_money, result = map(int, input().split())
    if move_money >= 0:
        cur += move_money
        if cur != result:
            print(-1)
            sys.exit()
    else:
        if -move_money <= cur:
            cur += move_money
            if cur != result:
                print(-1)
                sys.exit()
        else:
            is_charged = True
            after_charge = -move_money + result
            charged_money = after_charge - cur
            M_candidate.append(charged_money)  # 충전된 금액
            max_limit = max(max_limit, after_charge + move_money)
            cur = result

if not is_charged:
    print(1)
else:
    max_gcd = gcd_N(M_candidate)
    if max_gcd <= max_limit:
        print(-1)
        sys.exit()
    print(max_gcd)
    sys.exit()
