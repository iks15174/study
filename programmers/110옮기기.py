def extract_x(s_el):
    x_num = 0
    new_s_el = []
    for sidx, s in enumerate(s_el):
        new_s_el.append(s)
        if len(new_s_el) < 3:
            continue
        if "".join(new_s_el[-3 : ]) == "110":
            x_num += 1
            for _ in range(3):
                new_s_el.pop()
    return ("".join(new_s_el), x_num)
def solution(s):
    answer = []
    for s_el in s:
        if s_el.find("110") == -1:
            answer.append(s_el)
            continue
        new_s_el, num = extract_x(s_el)
        last_zero = new_s_el.rfind('0')
        if last_zero == -1:
            new_s_el = ("110" * num) + new_s_el
        else:
            new_s_el = new_s_el[0 : last_zero + 1] + ("110" * num) + new_s_el[last_zero + 1: ]
        answer.append(new_s_el)
            
        
    return answer