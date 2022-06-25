str1 = list(input())
str2 = list(input())
len1 = len(str1)
len2 = len(str2)
dp = [[0] * (len2 + 1) for _ in range((len1 + 1))]

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
r = len1
c = len2
result = []
while dp[r][c] != 0:
    if str1[r - 1] == str2[c - 1]:
        result.append(str1[r - 1])
        r -= 1
        c -= 1
    else:
        if dp[r][c - 1] > dp[r - 1][c]:
            c -= 1
        else:
            r -= 1
            
            
result = list(reversed(result))
print(dp[len1][len2])
if dp[len1][len2] != 0:
    print(''.join(result))