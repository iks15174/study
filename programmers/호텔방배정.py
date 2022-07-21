import sys
sys.setrecursionlimit(10**7)
def find_pos(r, allocate_dict):
    if r not in allocate_dict:
        allocate_dict[r] = r + 1
        return r
    allocate_dict[r] = find_pos(allocate_dict[r], allocate_dict)
    return allocate_dict[r]

def solution(k, room_number):
    answer = []
    allocate_dict = {}
    for r in room_number:
        answer.append(find_pos(r, allocate_dict))
            
    return answer