n = int(input())
n_list = []
cost = 10e9
for _ in range(n):
    n_list.append(int(input()))
n_list = sorted(n_list)


def calc(min, max):
    cost_val = 0
    for ni in n_list:
        if ni < min:
            cost_val += (min - ni) ** 2
        elif ni > max:
            cost_val += (ni - max) ** 2
    return cost_val


if n_list[-1] - n_list[0] > 17:
    for i in range(n_list[0], n_list[-1]):
        cost = min(cost, calc(i, i + 17))
if cost == 10e9:
    print(0)
else:
    print(cost)
