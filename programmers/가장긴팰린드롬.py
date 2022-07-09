def solution(s):
    answer = 1
    len_s = len(s)
    is_pelindrom = [[False] * len_s for _ in range(len_s)]
    for i in range(len_s):
        is_pelindrom[i][i] = True
        
    for i in range(len_s - 1):
        if s[i] == s[i + 1]:
            is_pelindrom[i][i + 1] = True
            answer = 2
        else:
            is_pelindrom[i][i + 1] = False
            
    for w in range(3, len_s + 1):
        for i in range(len_s - w + 1):
            if s[i] == s[i + w - 1] and is_pelindrom[i + 1][i + w - 2]:
                is_pelindrom[i][i + w - 1] = True
                answer = w
            else:
                is_pelindrom[i][i + w - 1] = False
            
    return answer