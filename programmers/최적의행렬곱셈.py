import math
dp = []
matrix = []
def solve(i, j): # matrix i ~ j 연산의 최솟값
    global dp, matrix
    if i >= j:
        dp[i][j] = 0
        return dp[i][j]
    if j == i + 1:
        dp[i][j] =  matrix[i][0] * matrix[i][1] * matrix[i + 1][1]
        return dp[i][j]
    if dp[i][j] != 0:
        return dp[i][j]
    ans = math.inf
    for pos in range(i, j):
        ans = min(ans, solve(pos + 1, j) + solve(i, pos) + matrix[i][0] * matrix[pos][1] * matrix[j][1])
    dp[i][j] = ans
    return dp[i][j]
    
def solution(matrix_sizes):
    global dp, matrix
    matrix = matrix_sizes
    len_m = len(matrix_sizes)
    dp = [[0] * len_m for _ in range(len_m)]
    solve(0, len_m - 1)
    answer = dp[0][len_m - 1]
    return answer

print(solution([[5,3],[3,10],[10,6]]))