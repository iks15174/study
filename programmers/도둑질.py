# dp[0][i]은 첫번째 집을 포함시켰을 때 i번까지의 집 범위에서 최대의 돈
# dp[1][i]는 첫번째 집을 포함시키지 않았을 때이다.
# 1, 2번쨰 집을 포함하지 않고, 3번째 집부터 시작해서 최대가 되는 경우도 있다는걸 주의해야 한다. 
def solution(money):
    dp = [[0] * 1000001 for _ in range(2)]
    dp[0][0] = money[0]
    dp[0][1] = money[0]
    dp[1][1] = money[1]
    dp[1][2] = money[1] 
    for i in range(2, len(money)):
        if i == len(money) - 1:
            dp[0][i] = dp[0][i - 1]
        else:
            dp[0][i] = max(dp[0][i - 2] + money[i], dp[0][i - 1])
        dp[1][i] = max(dp[1][i - 2] + money[i], dp[1][i - 1])
    return max(dp[0][len(money) - 1], dp[1][len(money) - 1])
        
    