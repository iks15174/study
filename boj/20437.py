import sys
import string
from collections import deque

input = sys.stdin.readline
test_case = int(input())

for _ in range(test_case):
    w_str = input().strip()
    k_int = int(input().strip())

    min_len = 10e5
    max_len = -1
    for char in string.ascii_lowercase:
        char_indexs = deque()
        for idx, w_char in enumerate(w_str):
            if w_char == char:
                char_indexs.append(idx)
                if len(char_indexs) == k_int:
                    min_len = min(min_len, char_indexs[-1] - char_indexs[0] + 1)
                    max_len = max(max_len, char_indexs[-1] - char_indexs[0] + 1)
                    char_indexs.popleft()

    if max_len == -1:
        print(-1)
    else:
        print(min_len, max_len)
