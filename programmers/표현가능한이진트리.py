def get_pad_len(l):
    l_bin = bin(l)[2:]
    return (2 ** len(l_bin)) - 1

def is_binary_possible(bin_str):
    if len(bin_str) == 1:
        if bin_str[0] == '1':
            return True
        return False
    
    if len(bin_str) == 3:
        if bin_str[1] == '1':
            return True
        elif bin_str == ''.join(['0'] * 3):
            return True
        return False
    
    if bin_str[len(bin_str) // 2] == '0':
        if bin_str == ''.join(['0'] * len(bin_str)):
            return True
        return False
        
    left_possible = is_binary_possible(bin_str[:len(bin_str) // 2])
    if not left_possible:
        return False
    
    right_possible = is_binary_possible(bin_str[len(bin_str) // 2 + 1:])
    if not right_possible:
        return False
            
    return True
    
def solution(numbers):
    answer = []
    for n in numbers:
        binary_n = bin(n)[2:]
        binary_n = binary_n.zfill(get_pad_len(len(binary_n)))
        if is_binary_possible(binary_n):
            answer.append(1)
        else:
            answer.append(0)
        
    return answer