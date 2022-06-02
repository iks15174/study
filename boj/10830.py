n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]


def mat_mul(matrix1, matrix2):
    global n
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for c in range(n):
                result[i][j] += (matrix1[i][c] * matrix2[c][j]) % 1000
            result[i][j] %= 1000
    return result


def solve(n, matrix):
    if n == 1:
        return matrix
    if n % 2 == 0:
        new_mat = solve(n / 2, matrix)
        return mat_mul(new_mat, new_mat)
    else:
        new_mat = solve(n - 1, matrix)
        return mat_mul(new_mat, matrix)


ans = solve(b, matrix)
for i in range(n):
    for j in range(n):
        ans[i][j] %= 1000
for l in ans:
    print(" ".join(map(str, l)))
