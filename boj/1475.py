import math

n = list(input())
num_count = [0 for i in range(10)]
for num in n:
    num_count[int(num)] += 1

sixNineSet = math.ceil((num_count[6] + num_count[9]) / 2)
num_count[9] = sixNineSet
num_count[6] = sixNineSet

print(max(num_count))
