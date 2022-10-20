a, b = map(int, input().split())
max_len = 55
acc = [0] * max_len

for i in range(1, max_len):
    acc[i] = 2 * acc[i - 1] + 2 ** (i - 1)

def get_ones(num):
    global acc, max_len
    ans = 0
    for bit in range(max_len - 1, 0, -1):
        if num & (1 << (bit - 1)):
            num -= (1 << (bit - 1))
            ans += acc[bit - 1] + num + 1
    return ans
print(get_ones(b) - get_ones(a - 1))
