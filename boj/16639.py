n = int(input())
num = n // 2 + 1  # 숫자의 갯수이다.
expression = list(input())
min_cal = [[0] * num for _ in range(num)]  # i ~ j 연산결과의 최솟값
max_cal = [[0] * num for _ in range(num)]  # i ~ j 연산결과의 최댓값


def cal(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2


for i in range(num):
    min_cal[i][i] = int(expression[i * 2])
    max_cal[i][i] = int(expression[i * 2])

for i in range(1, num):  # 연산을 위한 간격
    for j in range(0, num - i):  # 연산 시작 부분의미
        min_val = 10e9
        max_val = -10e9
        for k in range(j, j + i):
            op = expression[k * 2 + 1]
            max_val = max(max_val, cal(max_cal[j][k], max_cal[k + 1][j + i], op))
            min_val = min(min_val, cal(max_cal[j][k], max_cal[k + 1][j + i], op))

            max_val = max(max_val, cal(max_cal[j][k], min_cal[k + 1][j + i], op))
            min_val = min(min_val, cal(max_cal[j][k], min_cal[k + 1][j + i], op))

            max_val = max(max_val, cal(min_cal[j][k], max_cal[k + 1][j + i], op))
            min_val = min(min_val, cal(min_cal[j][k], max_cal[k + 1][j + i], op))

            max_val = max(max_val, cal(min_cal[j][k], min_cal[k + 1][j + i], op))
            min_val = min(min_val, cal(min_cal[j][k], min_cal[k + 1][j + i], op))

        max_cal[j][j + i] = max_val
        min_cal[j][j + i] = min_val

print(max_cal[0][num - 1])
