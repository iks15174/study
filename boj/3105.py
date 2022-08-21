n = int(input())
line = [int(input()) for _ in range(n)]
s = []
ans = 0
for l in line:
    if len(s) == 0:
        s.append(l)
    elif s[-1] > l:
        ans += 1
        s.append(l)
    elif s[-1] < l:
        while s and s[-1] < l:
            s.pop()
            ans += 1
        if s:
            ans += 1
        s.append(l)
    else:
        for idx in range(len(s) - 1, -1, -1):
            if s[idx] == l:
                ans += 1
            else:
                ans += 1
                s.append(l)
                break
            
print(ans)
            