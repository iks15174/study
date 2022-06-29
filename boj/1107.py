n = int(input())
broken = int(input())
brk_num = []
brk_dict = [True] * 10
max_num = 1000000
if broken != 0:
    brk_num = list(map(int, input().split()))
for b in brk_num:
    brk_dict[b] = False

def can_make(num):
    global brk_num
    for n1 in str(num):
        if not brk_dict[int(n1)]:
            return False
    return True

ans = abs(n - 100)
for i in range(max_num + 1):
    if can_make(i):
        ans = min(ans, abs(n - i) + len(str(i)))
print(ans)    