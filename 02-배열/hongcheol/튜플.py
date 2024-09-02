import pandas as pd
def solution(s):
    answer = []
    s=s.replace('{',',').replace('}',',')
    s=s[1:-1].split(',')
    temp=pd.DataFrame(s)
    #print(temp.value_counts().index[1])
    indexx=list(temp.value_counts().index)
    for i in indexx[1:]:
        answer.append(int(i[0]))
        #print(indexx[i]*1)
    print(answer)
    return answer
