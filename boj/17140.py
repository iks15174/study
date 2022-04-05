from itertools import groupby

ans_r, ans_c, k = map(int, input().split())
ans_r -= 1
ans_c -= 1
row = 3
col = 3
matrix = [[0] * (101) for _ in range(101)]
for r in range(3):
    line = list(map(int, input().split()))
    for c in range(len(line)):
        matrix[r][c] = line[c]

ans = 0
while ans <= 100:
    # print("--------debug-------------")
    # for i in range(10):
    #     print(matrix[i][0:10])
    if matrix[ans_r][ans_c] == k:
        break
    if row >= col:
        for idx, r in enumerate(matrix):
            new_list = groupby(sorted(list(filter(lambda u: u != 0, r))), lambda x: x)
            for j in range(101):
                matrix[idx][j] = 0
            res_list = []
            for n in new_list:
                cnt = 0
                for iter in n[1]:
                    cnt += 1
                res_list.append((n[0], cnt))  # 수와 수가 등장한 횟수를 저장한다.
            # 등장횟수 그리고 수의 크기 순으로 정렬
            res_list = sorted(res_list, key=lambda x: (x[1], x[0]))
            res_list = [y for x in res_list for y in x]
            res_list = res_list[0:101]
            col = max(col, len(res_list))

            for idx2, r in enumerate(res_list):
                matrix[idx][idx2] = r

    else:
        for c in range(101):
            new_list = []
            for r in range(101):
                new_list.append(matrix[r][c])
                matrix[r][c] = 0
            new_list = groupby(
                sorted(list(filter(lambda u: u != 0, new_list))), lambda x: x
            )
            res_list = []
            for n in new_list:
                cnt = 0
                for iter in n[1]:
                    cnt += 1
                res_list.append((n[0], cnt))  # 수와 수가 등장한 횟수를 저장한다.
            # 등장횟수 그리고 수의 크기 순으로 정렬
            res_list = sorted(res_list, key=lambda x: (x[1], x[0]))
            res_list = [y for x in res_list for y in x]
            res_list = res_list[0:101]
            row = max(row, len(res_list))

            for r in range(len(res_list)):
                matrix[r][c] = res_list[r]
    ans += 1

if ans > 100:
    print(-1)
else:
    print(ans)
