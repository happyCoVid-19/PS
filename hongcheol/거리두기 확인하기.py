def solution(places):
    abc=[]
    abc=places
    answer=[1,1,1,1,1]
    for i in range(5): #방 5개
        for j in range(5): #열 5개
            for p in range(5): #행 5개 
                if (abc[i][j][p]=='P'): #옆에 친구 구경
                    for q in range(1,3):
                        if (p+q<5):
                            if (abc[i][j][p+q]=='X'):
                                break
                            if (abc[i][j][p+q]=='P'):
                                #print('error',i,'type1')
                                answer[i]=0
                    for q in range(1,3):
                        if (j+q<5):
                            if (abc[i][j+q][p]=='X'):
                                break
                            if (abc[i][j+q][p])=='P':
                                #print('error',i,'type2')
                                answer[i]=0
                    if (j+1<5 and p+1<5):
                        if (abc[i][j+1][p+1]=='P'):
                            if (abc[i][j][p+1]=='X' and abc[i][j+1][p]=='X'):
                                print('pass')
                            else:
                                #print('error',i,'type3')
                                answer[i]=0
                    if (j+1<5 and p-1>=0):
                        if (abc[i][j+1][p-1]=='P'):
                            if (abc[i][j][p-1]=='X' and abc[i][j+1][p]=='X'):
                                print('pass')
                            else:
                                #print('error',i,'type4')
                                answer[i]=0
        
                            
            
    return answer
