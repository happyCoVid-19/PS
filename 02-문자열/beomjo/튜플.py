from collections import defaultdict
def solution(s):
    dic = defaultdict(int)
    s = eval(s.replace("{", "[").replace("}", "]"))
    for s_tuple in s:
        for s_element in s_tuple:
            dic[s_element] += 1
    answer = [num[0] for num in sorted(dic.items(), key = lambda x: x[1], reverse = True)]
    
    return answer