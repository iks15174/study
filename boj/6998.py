n = int(input())
nums = list(map(int, input().split()))
nums_pos = [-1] * 1000001
# nums[i], nums[j] 차이에 대한 수열 계산이 완료됐는지 확인하는 배열이다.
computed = [[False] * len(nums) for _ in range(len(nums))]
ans = 0
for idx, num in enumerate(nums):
    nums_pos[num] = idx

for i in range(len(nums)):
    for j in range(i + 1, len(nums), 1):
        if computed[i][j]:
            continue
        diff = nums[j] - nums[i]
        third_num = nums[j] + diff
        sum = nums[i] + nums[j]
        len_bigger_three = False
        while third_num <= 1000000 and nums_pos[third_num] != -1:
            computed[nums_pos[third_num - diff]][nums_pos[third_num]] = True
            sum += nums[nums_pos[third_num]]
            third_num += diff
            len_bigger_three = True

        if len_bigger_three:
            ans = max(ans, sum)

print(ans)
