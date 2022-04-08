def prime_list(n):
    n = n + 1
    is_prime = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if is_prime[i] == True:
            for j in range(2 * i, n, i):
                is_prime[j] = False

    return [i for i in range(2, n) if is_prime[i]]


n = int(input())
count = 0
start = 0
end = 0
interval_sum = 0
prime_nums = prime_list(n)
while True:
    if interval_sum >= n:
        if interval_sum == n:
            count += 1
        interval_sum -= prime_nums[start]
        start += 1
    elif end == len(prime_nums):
        break
    else:
        interval_sum += prime_nums[end]
        end += 1

print(count)
