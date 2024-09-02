import re

def solution(s):
    answer = []
    
    s = s[1:-1]
    ss = re.sub("{|},{|}", " ", s)
    sss = ss.split(" ")[1:-1]
    sss.sort(key=len)
    
    for i in sss:
        temp = i.split(",")
        for j in temp:
            if int(j) not in answer:
                answer.append(int(j))
            
    return answer