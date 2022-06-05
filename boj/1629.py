a, b, c = map(int, input().split())


def solve(n):
    global a, c
    if n == 1:
        return a % c
    if n == 0:
        return 1
    if n % 2 == 0:
        val = solve(n // 2)
        return (val ** 2) % c
    else:
        val = solve(n - 1)
        return (val * a) % c


print(solve(b))
