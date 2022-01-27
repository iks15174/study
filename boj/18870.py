num_len = map(int, input())
num_list = list(map(int, input().split()))
new_list = list(set(num_list))  # 중복제거 후 리스트 만들기
new_list.sort()
new_list_dic = {}
for index, item in enumerate(new_list):
    new_list_dic[item] = index

print(" ".join(list(map(lambda num: str(new_list_dic[num]), num_list))))
