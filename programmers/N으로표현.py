def solution(N, number):
    dp = [[] for _ in range(9)]
    basic_num = str(N)
    for i in range(1, 9):
        if number == int(basic_num):
            return i
        dp[i].append(int(basic_num))
        basic_num += str(N)
    
    for i in range(2, 9):
        for k in range(1, i // 2 + 1):
            for n1 in dp[k]:
                for n2 in dp[i - k]:
                    result = [n1 * n2, n1 - n2, n2 - n1, n1 + n2]
                    if n2 != 0:
                        result.append(n1 // n2)
                    if n1 != 0:
                        result.append(n2 // n1)
                    if number in result:
                        return i
                    dp[i].extend(result)
            
    return -1