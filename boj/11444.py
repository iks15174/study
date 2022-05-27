"""
점화식을 매트릭스 연산으로 바꿔서 분할정복을 통해 풀 수 있도록 만든 문제이다.
n의 수가 1억이상이라 반드시 logn 연산으로 바꿔야 할 경우
생각해 볼 수 있는 풀이이다.
"""
import sys

sys.setrecursionlimit(10 ** 8)
n = int(input())
matrix = [[1, 1], [1, 0]]
f1 = 0
f2 = 1
mod = 1000000007


def matrix_real_mul(m1, m2):
    length = len(m1)
    result = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            for k in range(length):
                result[i][j] += m1[i][k] * m2[k][j]
            result[i][j] %= mod
    return result


def matrix_mul(mat, num):
    if num == 1:
        return mat
    if num % 2 == 0:
        result = matrix_mul(mat, num // 2)
        return matrix_real_mul(result, result)
    else:
        return matrix_real_mul(matrix_mul(mat, num - 1), mat)


fibo_matrix = matrix_mul(matrix, n - 1)
print((f2 * fibo_matrix[0][0] + f1 * fibo_matrix[0][1]) % mod)
