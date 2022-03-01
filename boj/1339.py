n = int(input())
word_to_num = {}  # 알파벳 숫자 쌍 저장 딕션너리
word_value = {}  # 각 알파벳의 가치를 나타내는 딕션너리이다.

for _ in range(n):
    word = input()
    for idx, w in enumerate(word):
        if w in word_value:
            word_value[w] += pow(
                10, len(word) - idx - 1
            )  # 사전에 값이 있다면 더해준다. 자릿수만큼 더해준다.
        else:
            word_value[w] = pow(10, len(word) - idx - 1)  # 사전에 값이 없다면 넣어준다.

sorted_word_value = sorted(
    word_value.items(), key=lambda item: item[1], reverse=True
)  # 가치 크기별로 내림차순으로 정렬

num = 9
result = 0
for word in sorted_word_value:
    result += word[1] * num  # 가치에 알맞은 숫자를 곱해서 구한다. ex) 222(가장큰 가치) * 9
    num -= 1

print(result)
