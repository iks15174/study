import statistics
import math

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

sorted_nums = sorted(nums)
most_freq = -1
prev = sorted_nums[0]
cur_freq = 1
for idx in range(1, len(sorted_nums)):
    if sorted_nums[idx] == prev:
        cur_freq += 1
    else:
        most_freq = max(most_freq, cur_freq)
        cur_freq = 1
        prev = sorted_nums[idx]
most_freq = max(most_freq, cur_freq)

prev = sorted_nums[0]
cur_freq = 1
freq_val = sorted_nums[0]
find_val = 0
for idx in range(1, len(sorted_nums)):
    if sorted_nums[idx] == prev:
        cur_freq += 1
    else:
        if cur_freq == most_freq and find_val < 2:
            freq_val = prev
            find_val += 1
        cur_freq = 1
        prev = sorted_nums[idx]

if cur_freq == most_freq and find_val < 2:
    freq_val = prev
    find_val += 1

print(round(statistics.mean(nums)))
print(sorted_nums[len(nums) // 2])
print(freq_val)
print(max(nums) - min(nums))
