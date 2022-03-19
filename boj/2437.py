n = int(input())
n_list = list(map(int, input().split()))

n_list = sorted(n_list)
if n_list[0] != 1:
    print(1)
else:
    possible_sum = 1  # 가장 앞의 1을 제외하고 시작
    for i in range(1, n):
        if possible_sum + 1 >= n_list[i]:
            possible_sum += n_list[i]
        else:
            break

    print(possible_sum + 1)
