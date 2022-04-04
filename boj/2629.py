weight_len = int(input())
weights = list(map(int, input().split()))
dp = [[] for _ in range(weight_len)]  # dp[i]는 i번째 까지의 구슬을 사용하여 만들 수 있는 무게의 집합이다.
dp[0] = set([weights[0], 0])
weight_possible = [False] * 40001  # 특정 무게를 만들 수 있는지 여부를 나타낸다.

# dp 배열 초기화
for i in range(1, weight_len):
    prev_weights = dp[i - 1]
    dp[i] = set()
    for prev_weight in prev_weights:
        dp[i].add(prev_weight + weights[i])  # 이전의 무게에 현재 추를 더한다
        dp[i].add(abs(prev_weight - weights[i]))  # 이전의 무게에 현재 추를 뺀다
        dp[i].add(prev_weight)  # 현재 추는 사용하지 않는다.

    for pos_weight in dp[i]:
        weight_possible[pos_weight] = True  # 가능한 무게 표시

# 테스트 실행
test = int(input())
test_num = list(map(int, input().split()))
for num in test_num:
    if weight_possible[num]:
        print("Y")
    else:
        print("N")
