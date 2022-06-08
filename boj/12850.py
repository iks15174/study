d = int(input())
geo_matrix = [
    [0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0],
]
start = [[1], [0], [0], [0], [0], [0], [0], [0]]
mod = 1000000007


def matrix_mul(a, b):
    result = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for c in range(len(b)):
                result[i][j] += a[i][c] * b[c][j]
            result[i][j] %= mod
    return result


def solve(n):
    if n == 1:
        return geo_matrix
    if n % 2 == 0:
        m = solve(n // 2)
        return matrix_mul(m, m)
    else:
        m = solve(n - 1)
        return matrix_mul(geo_matrix, m)


move = solve(d)
result = matrix_mul(move, start)
print(result[0][0] % mod)
