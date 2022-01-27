a, d, k = map(int, input().split())
d = d / 100
k = k / 100
avg = 0
try_count = 1  # try_count 횟수만에 성공하는 확률을 구하는 것이다.
fail = 1  # 게임에서 질 확률이다.
while d < 1:
    avg += a * try_count * d * fail
    try_count += 1
    fail *= 1 - d  # try_count - 1 번의 시도를 질 확률
    d = d + d * k
avg += a * try_count * fail  # 이길확률이 100%를 넘었을 때
print(avg)
