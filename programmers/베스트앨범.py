def solution(genres, plays):
    g_dic = {}
    for idx, num in enumerate(plays):
        g = genres[idx]
        if g in g_dic:
            g_dic[g]['total'] += num
            g_dic[g]['arr'].append([num, idx])
        else:
            g_dic[g] = {'total' : num, 'arr' : [[num, idx]]}
    for k, i in g_dic.items():
        g_dic[k]['arr'] = sorted(g_dic[k]['arr'], key = lambda x : (-x[0], x[1]))
    g_dic = dict(sorted(g_dic.items(), key = lambda x : -x[1]['total']))
    ans = []
    for k, i in g_dic.items():
        if len(i['arr']) > 1:
            ans.append(i['arr'][0][1])
            ans.append(i['arr'][1][1])
        else:
            ans.append(i['arr'][0][1])
    return ans