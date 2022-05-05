from collections import deque

n = int(input())
strlist = deque([])
for _ in range(n):
    strlist.append(input())


def check(strlist, start, end):
    if strlist[start] > strlist[end]:
        return "back"
    elif strlist[start] < strlist[end]:
        return "front"
    else:
        if end - start <= 1:
            return "front"
        return check(strlist, start + 1, end - 1)


ans = ""
for i in range(1, n + 1):
    if check(strlist, 0, len(strlist) - 1) == "front":
        ans += strlist.popleft()
    else:
        ans += strlist.pop()
    if i % 80 == 0:
        ans += "\n"

print(ans)
