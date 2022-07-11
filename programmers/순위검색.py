import bisect

def to_hashs(lang, position, year, food):
    hashs = 0
    if lang == "java":
        hashs += 1000 * 1
    elif lang == "cpp":
        hashs += 1000 * 2
    elif lang == "python":
        hashs += 1000 * 3
        
    if position == "backend":
        hashs += 1 * 100
    elif position == "frontend":
        hashs += 2 * 100
    
    if year == "junior":
        hashs += 1 * 10
    elif year == "senior":
        hashs += 2 * 10
        
    if food == "chicken":
        hashs += 1
    elif food == "pizza":
        hashs += 2
    return hashs

def solution(info, query):
    info_dict = {}
    for i in info:
        lang, position, year, food, score = i.split()
        hash_k = to_hashs(lang, position, year, food)
        if hash_k not in info_dict:
            info_dict[hash_k] = [int(score)]
        else:
            info_dict[hash_k].append(int(score))
    for key, val in info_dict.items():
        info_dict[key] = sorted(val)
    
    answer = []
    for q in query:
        lang, _, position, _, year, _, food, score = q.split()
        score = int(score)
        keys = []
        lang = ["java", "python", "cpp"] if lang == "-" else [lang]
        position = ["backend", "frontend"] if position == "-" else [position]
        year = ["junior", "senior"] if year == "-" else [year]
        food = ["chicken", "pizza"] if food == "-" else [food]
        
        for l in lang:
            for p in position:
                for y in year:
                    for f in food:
                        keys.append(to_hashs(l, p, y, f))
        cnt = 0
        for k in keys:
            if k not in info_dict:
                continue
            arr = info_dict[k]
            # right = bisect.bisect_left(arr, int(score)) python built in 함수라 최적화가 되어 있어 더 빠르다.
            left = 0
            right = len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] < score:
                    left = mid + 1
                else:
                    right = mid
            cnt += (len(arr) - right)
        
        answer.append(cnt)
        
    return answer