import math

n, m = map(int, input().split())
cost = 0
min_package = math.inf
min_individual = math.inf
for _ in range(m):
    package, individual = map(int, input().split())
    min_package = min(min_package, package)
    min_individual = min(min_individual, individual)

if 6 * min_individual < min_package:
    cost = min_individual * n
else:
    package_cost = (n // 6) * min_package
    if n % 6 == 0:
        cost = package_cost
    else:
        cost = min(
            package_cost + min_package, package_cost + ((n % 6) * min_individual)
        )

print(cost)
