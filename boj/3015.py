n = int(input())
line = [int(input()) for _ in range(n)]
s = []
ans = 0
for l in line:
    if len(s) == 0:
        s.append([l, 1])
    elif s[-1][0] > l:
        ans += 1
        s.append([l, 1])
    elif s[-1][0] < l:
        while s and s[-1][0] < l:
            val, cnt = s.pop()
            ans += cnt
        if s and s[-1][0] == l:
            val, cnt = s.pop()
            ans += cnt
            if s:
                ans += 1
            s.append([l, cnt + 1])
        else:
            if s:
                ans += 1
            s.append([l, 1])
    else:
        val, cnt = s.pop()
        ans += cnt
        if s:
            ans += 1
        s.append([l, cnt + 1])
        
            
print(ans)