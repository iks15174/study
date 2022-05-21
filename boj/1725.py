import sys

input = sys.stdin.readline
n = int(input().strip())
nums = [int(input().strip()) for _ in range(n)]
st = []
ans = -1
for i in range(n):
    while st and st[-1][0] > nums[i]:
        value = st.pop()
        w = i
        if st:
            w -= st[-1][1] + 1
        ans = max(ans, w * value[0])
    st.append((nums[i], i))
# 최종적으로 남은 결과물은 bar의 오름차순이다.
while st:
    value = st.pop()
    w = n
    if st:
        w -= st[-1][1] + 1
    ans = max(ans, w * value[0])
print(ans)
