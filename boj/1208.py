# n, s = map(int, input().split())
# nums = list(map(int, input().split()))
# ans = 0
# subset_sum1 = []
# subset_sum2 = []
# subset1 = nums[0 : len(nums) // 2]
# subset2 = nums[len(nums) // 2 :]


# def lower_bound(value, arr):
#     left = 0
#     right = len(arr)
#     while left < right:
#         mid = (left + right) // 2
#         if arr[mid] < value:
#             left = mid + 1
#         elif arr[mid] > value:
#             right = mid
#         else:
#             right = mid
#     return right


# def upper_bound(value, arr):
#     left = 0
#     right = len(arr)
#     while left < right:
#         mid = (left + right) // 2
#         if arr[mid] < value:
#             left = mid + 1
#         elif arr[mid] > value:
#             right = mid
#         else:
#             left = mid + 1
#     return right


# def solve(idx, sum, type):
#     global ans, subset1, subset2, subset_sum1, subset_sum2
#     arr = subset1 if type == 1 else subset2
#     subset_sum = subset_sum1 if type == 1 else subset_sum2

#     if idx >= len(arr):
#         return
#     sum += arr[idx]
#     subset_sum.append(sum)
#     if sum == s:
#         ans += 1

#     solve(idx + 1, sum, type)
#     solve(idx + 1, sum - arr[idx], type)


# solve(0, 0, 1)
# solve(0, 0, 2)
# subset_sum2 = sorted(subset_sum2)
# for sb1 in subset_sum1:
#     lower = lower_bound(s - sb1, subset_sum2)
#     upper = upper_bound(s - sb1, subset_sum2)
#     if subset_sum2[upper - 1] == s - sb1:
#         ans += upper - lower
# print(ans)

n, s = map(int, input().split())
nums = list(map(int, input().split()))
left_nums = nums[:len(nums) // 2]
right_nums = nums[len(nums) // 2:]
left_dict = {}
right_dict = {}

def solve(arr, idx, sum, dic):
    if idx == len(arr):
        if sum in dic:
            dic[sum] += 1
        else:
            dic[sum] = 1
        return
    
    solve(arr, idx + 1, sum, dic)
    solve(arr, idx + 1, sum + arr[idx], dic)
    
solve(left_nums, 0, 0, left_dict)
solve(right_nums, 0, 0, right_dict)

ans = 0
for k, i in left_dict.items():
    val = s - k
    if val in right_dict:
        ans += (i * right_dict[val])
if s == 0:
    ans -= 1
print(ans) 
