## 다시 풀어볼것
import sys
import string
import heapq

input = sys.stdin.readline
s = input().strip()
t = input().strip()
min_len = 1  # 최소한의 반복 횟수이다.
s_char_dic = {}  # s에 포함된 알파벳의 갯수를 의미한다.
t_char_index_dic = {}  # t에 포함된 알파벳의 index를 의미한다
t_char_dic = {}  # t에 포함된 알파벳의 갯수를 의미한다.


def binary_search(char_list, last_t_index):  # char_list는 현재 찾아야 하는 문자의 인데스들이 담겨있는 배열이다.
    left = 0
    right = len(char_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if char_list[mid] > last_t_index:
            right = mid - 1
        elif char_list[mid] < last_t_index:
            left = mid + 1
        else:
            if mid + 1 < len(char_list):
                return char_list[mid + 1]
            else:
                return -1  # 적절한 index를 찾지 못했을 때

    if left < len(char_list):
        return char_list[left]
    else:
        return -1


for lower_char in string.ascii_lowercase[:26]:
    s_char_dic[lower_char] = 0
    t_char_dic[lower_char] = 0

# 각 배열의 dictionary를 업데이트 해준다.
for char in s:
    s_char_dic[char] += 1

for char in t:
    t_char_dic[char] += 1

# t_char_dic 은 char과 char이 존재하는 index list(작은순으로 정렬)의 집합이다.
for idx, char in enumerate(t):
    if char in t_char_index_dic:
        # print(t_char_dic[char])
        heapq.heappush(t_char_index_dic[char], idx)
    else:
        t_char_index_dic[char] = []
        heapq.heappush(t_char_index_dic[char], idx)


s_set = set([key for key, value in s_char_dic.items() if value > 0])
t_set = set([key for key, value in t_char_dic.items() if value > 0])


# t를 아무리 반복해도 s에는 t에 없는 문자가 있기 때문에 줄임말을 만들 수 없다.
if len(s_set - t_set) > 0:
    print(-1)

else:
    last_t_index = -1  # 마지막으로 참고한 t 문자열의 index를 의미한다.
    i = 0
    while i < len(s):
        s_char = s[i]
        t_char_indexes = t_char_index_dic[s_char]
        indexes = binary_search(t_char_indexes, last_t_index)
        if indexes == -1:
            min_len += 1
            last_t_index = -1
            i -= 1
        else:
            last_t_index = indexes

        i += 1

    print(min_len)
