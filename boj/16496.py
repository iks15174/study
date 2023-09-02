import functools
n = int(input())
nums = list(input().split())

def repeat_num(num, length):
    result = ''
    idx = 0
    while idx < length:
        result += num[idx % len(num)]
        idx += 1
    return result

def compare(a, b):
    s1 = a + b
    s2 = b + a
    if s1 > s2:
        return -1
    else:
        return 1
        
    
sorted_nums = sorted(nums, key=functools.cmp_to_key(compare))
answer = sorted_nums[0] if sorted_nums[0] == '0' else sorted_nums
print(''.join(answer))

'''
반례
10
1 111101111 1011111 10 10101010 101101110 101010101 111111111 111111110 1011111

ans: 1111111111111111110111101111101111110111111011011101010101011010101010
     1111111111111111110111101111101111110111111011011101010101011010101010
출처: https://www.acmicpc.net/board/view/79325


96722787324582684682681256980744176024875360874135766818864962563334362389844721636433924548242191175610166171156711155969
96722787324582684682681256980744176024875360874135766818864962563334362389844721636433924548242191175610166171156711155969
'''