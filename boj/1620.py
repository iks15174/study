import enum


n, m = map(int, input().split())
pocketmon_list = []
pocketmon_list_dic = {}

for i in range(n):
    name = input()
    pocketmon_list.append(name)
    pocketmon_list_dic[name] = i + 1

for i in range(m):
    problem = input()
    if problem.isnumeric():
        print(pocketmon_list[int(problem) - 1])
    else:
        print(pocketmon_list_dic[problem])

## pypy 환경에서 돌려야 통과함
