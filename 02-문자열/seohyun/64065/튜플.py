def solution(s):
    strs = s.split('},{')
    for i in range(len(strs)):
        strs[i] = strs[i].replace('{', '').replace('}', '')
    
    strs.sort(key=len)
    
    answer = []
    for i in strs:
        str = i.split(',')
        for src in str:
            if int(src) not in answer:
                answer.append(int(src))
        
    return answer