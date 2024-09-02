def solution(s):
    count_zero=0
    total=0
    value=s
    total_try=0
    while(len(value)!=1):
        total=0
        total_try+=1
        for i in value:
            if(i=='1'):
                total+=1
            if(i=='0'):
                count_zero+=1
        value=bin(total)[2:]
        print(value)
    answer = []
    answer.append(total_try)
    answer.append(count_zero)
    return answer
