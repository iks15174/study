# t = int(input())
# pado_num = [-1 for _ in range(105)]
# pado_num[0] = 1
# pado_num[1] = 1
# pado_num[2] = 1
# pado_num[3] = 2
# pado_num[4] = 2


# def solve(n):
#     if pado_num[n] != -1:
#         return pado_num[n]

#     pado_num[n] = solve(n - 2) + solve(n - 3)
#     return pado_num[n]


# for i in range(t):
#     n = int(input())
#     n = n - 1
#     if n < 5:
#         print(pado_num[n])
#         break
#     print(solve(n))

t = int(input())
 
li = [1,1,1,2,2]
for i in range(5, 100):
    li.append(li[i-1]+li[i-5])
 
for _ in range(t):
    n = int(input())
    print(li[n-1]))
