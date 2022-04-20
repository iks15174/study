import math

n = int(input())
liquids = list(map(int, input().split()))
start = 0
end = n - 1
ans_start = start
ans_end = end
cand = math.inf
while start < end:
    sum = liquids[start] + liquids[end]
    if abs(sum) < abs(cand):
        cand = sum
        ans_start = start
        ans_end = end
    if sum > 0:
        end -= 1
    elif sum < 0:
        start += 1
    else:
        break

print(liquids[ans_start], liquids[ans_end])
