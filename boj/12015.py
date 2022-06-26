import sys

input = sys.stdin.readline
n = int(input().strip())
nums = list(map(int ,input().strip().split()))
log = []

def lower_bound(val):
    global log
    left = 0
    right = len(log)
    while left < right:
        mid = (left + right) // 2
        if log[mid] < val:
            left = mid + 1
        else:
            right = mid
    return right

for nm in nums:
    if len(log) == 0 or log[-1] < nm:
        log.append(nm)
    else:
        log[lower_bound(nm)] = nm
    
print(len(log))    