from unittest import result


# 1부터 작은 수 차례대로 더해가다가, 다음에 더할 수가 남은 수보다 크다면, 이전에 다른 값을 더해서 끝내야 한다는 의미이다.
s = int(input())
natural_num = 1
sum = 0

while (s - sum) >= natural_num:
    sum += natural_num
    natural_num += 1

print(natural_num - 1)
